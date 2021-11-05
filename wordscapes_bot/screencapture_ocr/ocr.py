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
    bounding_boxes = [{}]
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        aspect_ratio = h / w
        if aspect_ratio > 0.8:
            # Crop the image so pytesseract can do character detection on the individual characters
            crop_img = img[y:y + h, x:x + w]
            # Add a border to the image so pytesseract can detect the character better
            crop_img = cv2.copyMakeBorder(crop_img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[255])

            conf = '--psm 10 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            character = pytesseract.image_to_string(crop_img, lang='eng', config=conf)

            characters.append(character[0:1])
            characters = [x.lower() for x in characters]
            bounding_boxes.append({'x': x, 'y': y, 'w': w, 'h': h})

    return {'characters': characters, 'bounding_boxes': bounding_boxes}


def ocr_bounding_boxes(image):
    img = image.copy()
    thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Find contours and filter using aspect ratio and area
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        aspect_ratio = h / w
        if aspect_ratio > 0.8:
            cv2.rectangle(img, (x, y), (x + w, y + h), (36, 255, 12), 2)

    return img
