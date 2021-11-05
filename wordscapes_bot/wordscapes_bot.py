from wordscapes_bot.word_search import word_search
from wordscapes_bot.wordscapes_ocr import get_formatted_screenshot
from wordscapes_bot.wordscapes_ocr import ocr_characters
from wordscapes_bot.wordscapes_input import input_word

import time
import cv2


class WordscapesBot:
    def __init__(self, word_palette_bbox):
        self.word_palette_bbox = word_palette_bbox
        # self.continue_location = continue_location

    def run(self):
        while True:
            loop_start_time = time.time()
            screenshot = get_formatted_screenshot(self.word_palette_bbox)

            characters = ocr_characters(screenshot)
            character_list = characters.keys()

            possible_words = word_search(character_list)

            for word in possible_words:
                input_word(word, characters)

            print(f'Loop finished in {loop_start_time - time.time()} s')
            time.sleep(5)
