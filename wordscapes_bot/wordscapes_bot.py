from wordscapes_bot.word_search import word_search
from wordscapes_bot.screencapture_ocr import get_formatted_screenshot
from wordscapes_bot.screencapture_ocr import ocr_characters

import time


class WordscapesBot:
    def __init__(self, word_palette_bbox):
        self.word_palette_bbox = word_palette_bbox
        # self.continue_location = continue_location

    def run(self):
        while True:
            loop_start_time = time.time()
            screenshot = get_formatted_screenshot(self.word_palette_bbox)
            characters = ocr_characters(screenshot)
            possible_words = word_search(characters['characters'])
            print(f'Loop finished in {loop_start_time - time.time()} s')
            time.sleep(5)
