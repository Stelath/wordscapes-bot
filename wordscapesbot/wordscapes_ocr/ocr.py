import pytesseract
import numpy as np
import cv2


def ocr_characters(image):
    img = image.copy()
    thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # Find contours and filter using aspect ratio and area
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    characters = []
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        area = h * w
        if area > 200:
            # Crop the image so pytesseract can do character detection on the individual characters
            crop_img = img[y:y + h, x:x + w]
            # Add a border to the image so pytesseract can detect the character better
            crop_img = cv2.copyMakeBorder(crop_img, 15, 15, 15, 15, cv2.BORDER_CONSTANT, value=[255])

            # Resize the image so that OCR is more accurate
            resize_width = 150
            resize_height = round(resize_width * (crop_img.shape[1] / crop_img.shape[0]))
            resized_image = cv2.resize(crop_img, (resize_width, resize_height))

            character_string = pytesseract.image_to_string(resized_image, lang='eng', config='--psm 10')[0:1]

            # Check for incorrect detections
            if character_string == 'l' or character_string == '|':
                character_string = 'i'
            elif character_string == '\x0c' or not character_string.isalpha():
                # Try again with stricter rules
                conf = '--psm 10 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ|'
                character_string = pytesseract.image_to_string(resized_image, lang='eng', config=conf)[0:1]

                # If there is still an error detecting the character return nothing
                if character_string == 'l' or character_string == '|':
                    character_string = 'i'
                elif character_string == '\x0c' or not character_string.isalpha():
                    return {}

            character_string = character_string.lower()

            character_position = {'x': x, 'y': y, 'w': w, 'h': h}
            characters.append([character_string, character_position])

    return characters


def ocr_bounding_boxes(image):
    img = image.copy()
    characters = ocr_characters(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    for character, pos in characters:
        x, y, w, h = (pos['x'], pos['y'], pos['w'], pos['h'])
        cv2.rectangle(img, (x, y), (x + w, y + h), (36, 255, 12), 2)

    return img
