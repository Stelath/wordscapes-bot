import pytesseract
import numpy as np
import cv2


def ocr_characters(image):
    img = image.copy()
    thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # Find contours and filter using aspect ratio and area
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    characters = {}
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        aspect_ratio = h / w
        if aspect_ratio > 0.8:
            # Crop the image so pytesseract can do character detection on the individual characters
            crop_img = img[y:y + h, x:x + w]
            # Add a border to the image so pytesseract can detect the character better
            crop_img = cv2.copyMakeBorder(crop_img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[255])

            conf = '--psm 10 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            character_string = pytesseract.image_to_string(crop_img, lang='eng', config=conf)[0:1].lower()
            print(character_string)
            character_position = {'x': x, 'y': y, 'w': w, 'h': h}
            characters[character_string] = character_position

    print(characters)
    return characters


def ocr_bounding_boxes(image):
    img = image.copy()
    characters = ocr_characters(img)
    for character in characters:
        x, y, w, h = (character['x'], character['y'], character['w'], character['h'])
        aspect_ratio = h / w
        if aspect_ratio > 0.8:
            cv2.rectangle(img, (x, y), (x + w, y + h), (36, 255, 12), 2)

    return img
