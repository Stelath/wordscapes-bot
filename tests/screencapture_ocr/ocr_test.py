import cv2
from wordscapes_bot.screencapture_ocr.get_image import screenshot
from wordscapes_bot.screencapture_ocr import get_formatted_screenshot
from wordscapes_bot.screencapture_ocr import ocr_characters
from wordscapes_bot.screencapture_ocr import ocr_bounding_boxes

screenshot_image = screenshot((79, 356, 234, 523))
formatted_image = get_formatted_screenshot((79, 356, 234, 523))
bounding_boxes = ocr_bounding_boxes(formatted_image)

characters = ocr_characters(formatted_image)
print(characters['characters'])
print(characters['bounding_boxes'])

cv2.imshow('screenshot', cv2.cvtColor(screenshot_image, cv2.COLOR_BGR2RGB))
cv2.imshow('formatted image', formatted_image)
cv2.imshow('bounding boxes', bounding_boxes)

while True:
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()