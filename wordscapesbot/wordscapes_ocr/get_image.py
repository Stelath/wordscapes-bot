import numpy as np
from PIL import ImageGrab
import cv2
from sys import platform


def screenshot(bounding_box):
    if platform != "darwin":
        img = np.array(ImageGrab.grab(bbox=bounding_box))
    else:
        print('On Mac OS')
        bounding_box = tuple([2 * num for num in bounding_box])
        img = ImageGrab.grab(bbox=bounding_box)
        # Set the image to half size so it works
        # when finding character pos on screens
        img = img.resize((round(img.size[0] * 0.5), round(img.size[1] * 0.5)))
        img = np.array(img)

    return img


# Used to make it easier for the OCR to detect the letters
def get_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def get_color_range(img, lower, upper):
    low = np.array(lower)
    upp = np.array(upper)
    mask = cv2.inRange(img, low, upp)
    return mask


def invert_image(img):
    inverted_img = cv2.bitwise_not(img)
    return inverted_img


def get_formatted_screenshot(bbox=(0, 40, 800, 640)):
    img = screenshot(bbox)
    img = get_grayscale(img)

    # Finds the color of the text by looking for the most common color in the
    # image that is <= 40 or >= 215
    unique, counts = np.unique(img.flatten(), axis=0, return_counts=True)
    for i in range(1, len(unique)):
        color = unique[np.where(counts == np.partition(counts.flatten(), -i)[-i])][0]
        if color <= 3 or color >= 252:
            break
    if not (color <= 3 or color >= 252):
        for i in range(1, len(unique)):
            color = unique[np.where(counts == np.partition(counts.flatten(), -i)[-i])][0]
            if color <= 40 or color >= 245:
                break
    img = get_color_range(img, color - 2, color + 2)
    img = invert_image(img)

    return img
