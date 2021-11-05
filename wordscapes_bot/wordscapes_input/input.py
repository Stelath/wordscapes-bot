from pynput.mouse import Button, Controller
import time


def input_word(word, input_characters):
    mouse = Controller()
    word_character_list = list(word)

    for character in word_character_list:
        character_position = input_characters[character]
        x = character_position['x'] + (character_position['w'] / 2)
        y = character_position['y'] + (character_position['h'] / 2)

        # mouse.position = (x, y)
        # mouse.press(Button.left)
        # print(f'Moved mouse to {mouse.position}')

        time.sleep(1)

    mouse.release(Button.left)
