import numpy as np
from PIL import ImageGrab
import cv2


def screenshot(bounding_box):
    printscreen = np.array(ImageGrab.grab(bbox=bounding_box))
    return printscreen


# Used to make it easier for the OCR to detect the letters
def get_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def get_white_color_range(img):
    lower = np.array([250])
    upper = np.array([255])
    mask = cv2.inRange(img, lower, upper)
    return mask


def invert_image(img):
    inverted_img = cv2.bitwise_not(img)
    return inverted_img


def get_formatted_image(bbox=(0, 40, 800, 640)):
    img = screenshot(bbox)
    img = get_grayscale(img)
    img = get_white_color_range(img)
    img = invert_image(img)
    return img
