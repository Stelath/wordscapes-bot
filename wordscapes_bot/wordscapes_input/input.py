from pynput.mouse import Button, Controller


def input_word(word, input_characters):
    mouse = Controller()
    word_character_list = list(word)

    mouse.press(Button.left)

    for character in word_character_list:
        character_position = input_characters[character]
        x = character_position['x'] + (character_position['w'] / 2)
        y = character_position['y'] + (character_position['h'] / 2)

        mouse.position = (x, y)

    mouse.release(Button.left)
