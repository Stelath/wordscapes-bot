import time
import cv2
from wordscapesbot.wordscapes_ocr import get_formatted_screenshot
from wordscapesbot.wordscapes_ocr.get_image import screenshot

start_time = time.time()
screenshot_image = screenshot((0, 40, 800, 640))
end_time = time.time()
print(f'Image capture took {end_time - start_time} seconds')

start_time = time.time()
formatted_image = get_formatted_screenshot()
end_time = time.time()
print(f'Image capture and processing took {end_time - start_time} seconds')

cv2.imshow('screenshot', screenshot_image)
cv2.imshow('formatted image', formatted_image)

while True:
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
