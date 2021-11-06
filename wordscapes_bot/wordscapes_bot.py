from wordscapes_bot.word_search import word_search
from wordscapes_bot.wordscapes_ocr import get_formatted_screenshot
from wordscapes_bot.wordscapes_ocr import ocr_characters
from wordscapes_bot.wordscapes_input import input_word

from pynput import keyboard
import time


class WordscapesBot:
    def __init__(self, word_palette_bbox):
        self.word_palette_bbox = word_palette_bbox
        self.run_active = True
        # self.continue_location = continue_location

    def on_release_key(self, key):
        if key == keyboard.Key.esc:
            print('ESC Key Pressed, Terminateing Program')
            quit()
            return False

    def run(self):
        # Add a way to stop the loop
        listener = keyboard.Listener(
            on_release=self.on_release_key)
        listener.start()

        while self.run_active:
            loop_start_time = time.time()
            screenshot = get_formatted_screenshot(self.word_palette_bbox)

            characters = ocr_characters(screenshot)
            character_list = list(characters.keys())
            print(characters)
            print(character_list)

            possible_words = word_search(character_list)
            print(possible_words)

            for word in possible_words:
                input_word(word, characters, self.word_palette_bbox)

            print(f'Loop finished in {loop_start_time - time.time()} s')
            time.sleep(7)
