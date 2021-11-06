from pynput.mouse import Button, Controller
import time


def input_word(word, in_characters, bbox):
    input_characters = in_characters.copy()

    mouse = Controller()
    word_character_list = list(word)

    bx, by, bx2, by2 = bbox

    for character in word_character_list:
        character_index = [character for character, pos in input_characters].index(character)
        character_position = input_characters[character_index][1]
        input_characters.pop(character_index)

        x = bx + (character_position['x'] + (character_position['w'] / 2))
        y = by + (character_position['y'] + (character_position['h'] / 2))

        mouse.position = (x, y)
        mouse.press(Button.left)

        time.sleep(0.1)

    mouse.release(Button.left)
    time.sleep(0.1)


def press_button(pos):
    mouse = Controller()
    mouse.position = pos
    mouse.click(Button.left)
