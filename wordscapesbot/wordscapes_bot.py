from .word_search import word_search
from .wordscapes_ocr import get_formatted_screenshot
from .wordscapes_ocr import ocr_characters
from .wordscapes_input import input_word
from .wordscapes_input import press_button
from .wordscapes_input import press_esc

import time


class WordscapesBot:
    def __init__(self, word_palette_bbox, level_button_loc, input_speed):
        self.word_palette_bbox = word_palette_bbox
        self.level_button_loc = level_button_loc
        self.run_active = True
        self.input_speed = input_speed

    def run(self):
        last_character_list = []
        failed = 1
        while self.run_active:
            loop_start_time = time.time()
            screenshot = get_formatted_screenshot(self.word_palette_bbox)

            characters = ocr_characters(screenshot)
            character_list = [character for character, pos in characters]

            # Check to see if the short dictionary could complete the puzzle,
            # if not use the long dictionary instead, this cuts down time overall
            # as the majority of puzzles can be completed with the short dictionary.
            # Also use a volitile way to detect characters in order to find the
            # correct character, although this is less accurate, it stops the bot
            # from getting stuck in a loop.
            if failed < 3:
                possible_words = word_search(character_list)
            elif failed < 5:
                possible_words = word_search(character_list, False)
            else:
                print('FAILED TOO MANY TIMES, ATTEMPTING VOLITILE CHARACTER OCR')
                characters = ocr_characters(screenshot, True)
                new_character_list = [character for character, pos in characters]
                possible_words = word_search(new_character_list, False)
            print('Characters Detected:', character_list)

            # Check to see if there is a popup in the way (the ocr
            # will not return any characters) and attempt to click out of it
            if not possible_words:
                esc = False
                press_button(self.level_button_loc)
                time.sleep(0.75)
                x1, y1, x2, y2 = self.word_palette_bbox
                press_button((x1 + ((x2 - x1) / 2), y2 + 40))
                time.sleep(0.25)
                press_button((x1 + ((x2 - x1) / 2), y1 + ((y2 - y1) / 2) + 10))
                failed += 1
            else:
                if character_list == last_character_list:
                    failed += 1
                else:
                    failed = 1
                last_character_list = character_list
                esc = True

            # Sort to increase chance of a bonus word
            possible_words = sorted(possible_words, key=len)
            print('Possible Words:', possible_words)

            for word in possible_words:
                input_word(word, characters, self.word_palette_bbox, self.input_speed)

            print(f'OCR and Input finished in {time.time() - loop_start_time} s\n')

            # Skip the animations and go to the next level with the esc key
            if esc:
                time.sleep(0.75)
                press_esc()
                press_button(self.level_button_loc)
                time.sleep(2.25)
