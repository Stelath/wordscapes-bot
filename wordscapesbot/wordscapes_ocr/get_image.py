import numpy as np
from PIL import ImageGrab, Image, ImageDraw
import cv2
from sys import platform


def screenshot(bounding_box):
    if platform != "darwin":
        img = np.array(ImageGrab.grab(bbox=bounding_box))
    else:
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


def circle_crop(img):
    # Crop the image in the shape of a circle
    w, h = img.shape
    xc, yc = w // 2, h // 2

    mask = np.zeros((w, h), np.uint8)
    circle_img = cv2.circle(mask, (xc, yc), yc, 255, -1)
    img = cv2.bitwise_and(img, img, mask=circle_img)
    return img


def color_mask_word_pallete(img):
    # Crop the image in the shape of a circle
    w, h = img.shape
    xc, yc = w // 2, h // 2

    base = np.full((w, h), 130, np.uint8)

    mask = np.full((w, h), 255, np.uint8)
    circle_img = cv2.circle(mask, (xc, yc), yc, 0, -1)
    color_mask = cv2.bitwise_and(base, base, mask=circle_img)
    for row in range(len(color_mask)):
        for col in range(len(color_mask[row])):
            if color_mask[row][col] == 0:
                color_mask[row][col] = img[row][col]

    color_mask = cv2.circle(color_mask, (xc, yc), int(yc - (w * 0.25)), 130, -1)
    return color_mask


def get_formatted_screenshot(bbox=(0, 40, 800, 640)):
    img = screenshot(bbox)
    img = get_grayscale(img)

    color_mask = color_mask_word_pallete(img)

    # Finds the color of the text by looking for the most common color in the
    # image that is <= 40 or >= 215
    unique, counts = np.unique(color_mask.flatten(), axis=0, return_counts=True)
    for i in range(1, len(unique)):
        color = unique[np.where(counts == np.partition(counts.flatten(), -i)[-i])][0]
        if color <= 3 or color >= 254:
            break
    if not (color <= 3 or color >= 252):
        for i in range(1, len(unique)):
            color = unique[np.where(counts == np.partition(counts.flatten(), -i)[-i])][0]
            if color <= 40 or color >= 245:
                break

    img = get_color_range(img, color - 2, color + 2)
    img = circle_crop(img)
    img = invert_image(img)

    return img
