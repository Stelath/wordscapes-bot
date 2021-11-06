from wordscapes_bot.word_search import word_search
from wordscapes_bot.wordscapes_ocr import get_formatted_screenshot
from wordscapes_bot.wordscapes_ocr import ocr_characters
from wordscapes_bot.wordscapes_input import input_word
from wordscapes_bot.wordscapes_input import press_button

import time


class WordscapesBot:
    def __init__(self, word_palette_bbox, level_button):
        self.word_palette_bbox = word_palette_bbox
        self.level_button = level_button
        self.run_active = True
        # self.continue_location = continue_location

    def run(self):
        while self.run_active:
            loop_start_time = time.time()
            screenshot = get_formatted_screenshot(self.word_palette_bbox)

            characters = ocr_characters(screenshot)
            character_list = [character for character, pos in characters]
            print(characters)
            print(character_list)

            possible_words = word_search(character_list)
            print(possible_words)

            for word in possible_words:
                input_word(word, characters, self.word_palette_bbox)

            print(f'OCR and Input finished in {loop_start_time - time.time()} s')

            time.sleep(8)
            press_button(level_button)
            time.sleep(4)
