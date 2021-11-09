from pynput import mouse
from pynput import keyboard
from .wordscapes_bot import WordscapesBot

import sys
import os

clicks = 0
level_button_pos = ()
word_palette_bbox = ()


def on_click_level(x, y, button, pressed):
    global level_button_pos
    if pressed:
        level_button_pos = (x, y)
        print(f'Pressed at {(x, y)}')

    return False


def on_click_bbox(x, y, button, pressed):
    global clicks
    global word_palette_bbox

    clicks += 1

    if pressed:
        word_palette_bbox += (x, y)
        print(f'Pressed at {(x, y)}')

    if clicks >= 4:
        return False
    elif clicks == 2:
        print('Please click on the bottom right corner of the word palette')


def on_release_key(key):
    if hasattr(key, 'char') and 'q' == key.char:
        print('Q Key Pressed, Terminating Program')
        os._exit(1)
        return False


def main():
    # Add a way to stop the loop
    listener = keyboard.Listener(
        on_release=on_release_key)
    listener.start()

    print('Please click the level start button')
    with mouse.Listener(
            on_click=on_click_level) as listener:
        listener.join()

    print('Please click on the top left corner of the word palette')
    with mouse.Listener(
            on_click=on_click_bbox) as listener:
        listener.join()

    print('Level Button Pos:', level_button_pos)
    print('Word Palette BBox:', word_palette_bbox)

    # Get the cli arguments passed when the package was run
    args = sys.argv[1:]
    input_speed = 1
    for i in range(len(args)):
        if args[i] == '-s' or args[i] == '--speed':
            input_speed = float(args[i+1])

    wordscapes_bot = WordscapesBot(word_palette_bbox, level_button_pos, input_speed)
    wordscapes_bot.run()


if __name__ == "__main__":
    main()
