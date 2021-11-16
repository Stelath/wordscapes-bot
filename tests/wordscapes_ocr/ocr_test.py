import cv2
from wordscapesbot.wordscapes_ocr.get_image import screenshot
from wordscapesbot.wordscapes_ocr import get_formatted_screenshot
from wordscapesbot.wordscapes_ocr import ocr_characters
from wordscapesbot.wordscapes_ocr import ocr_bounding_boxes

bbox = (1435, 586, 1773, 932)
screenshot_image = screenshot(bbox)
formatted_image = get_formatted_screenshot(bbox)
bounding_boxes = ocr_bounding_boxes(formatted_image)

characters = ocr_characters(formatted_image)
print([character for character, pos in characters])
print(characters)

cv2.imshow('screenshot', cv2.cvtColor(screenshot_image, cv2.COLOR_BGR2RGB))
cv2.imshow('formatted image', formatted_image)
cv2.imshow('bounding boxes', bounding_boxes)

while True:
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()