from pynput import mouse
from pynput import keyboard
from wordscapes_bot.wordscapes_bot import WordscapesBot

import sys
import os

clicks = 0
word_palette_bbox = ()


def on_click(x, y, button, pressed):
    global clicks
    global word_palette_bbox
    if pressed:
        word_palette_bbox += (x, y)
        print(f'Pressed at {(x, y)}')

    if clicks == 3:
        return False
    else:
        clicks += 1

def on_release_key(key):
    if key == keyboard.Key.esc:
        print('ESC Key Pressed, Terminating Program')
        os._exit(1)
        return False

def main():
    # Add a way to stop the loop
    listener = keyboard.Listener(
        on_release=on_release_key)
    listener.start()

    with mouse.Listener(
            on_click=on_click) as listener:
        listener.join()

    print(word_palette_bbox)
    wordscapes_bot = WordscapesBot(word_palette_bbox)
    wordscapes_bot.run()

if __name__ == "__main__":
    main()
