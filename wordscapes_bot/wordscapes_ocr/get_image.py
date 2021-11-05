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


def get_black_color_range(img):
    lower = np.array([0])
    upper = np.array([5])
    mask = cv2.inRange(img, lower, upper)
    return mask


def invert_image(img):
    inverted_img = cv2.bitwise_not(img)
    return inverted_img


def get_formatted_screenshot(bbox=(0, 40, 800, 640)):
    img = screenshot(bbox)
    img = get_grayscale(img)

    number_of_white_pix = np.sum(img >= 250)
    number_of_black_pix = np.sum(img <= 5)
    if number_of_white_pix > number_of_black_pix:
        img = get_white_color_range(img)
        img = invert_image(img)
    else:
        img = get_black_color_range(img)
        img = invert_image(img)

    return img
