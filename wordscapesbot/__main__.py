from pynput import mouse
from pynput import keyboard
from .wordscapes_bot import WordscapesBot

import sys
import os
import time

clicks = 0
level_button_pos = ()
word_palette_bbox = ()

piggy_close_pos = ()
edge_close_pos = ()
button_clicks = 0


def on_click_buttons(x, y, button, pressed):
    global button_clicks
    global level_button_pos
    global piggy_close_pos
    global edge_close_pos

    button_clicks +=1

    if pressed:
        if button_clicks == 1:
            piggy_close_pos = (x, y)
        elif button_clicks == 3:
            edge_close_pos = (x, y)
        else:
            level_button_pos = (x, y)
        print(f'Pressed at {(x, y)}')

    if button_clicks >= 6:
        return False
    elif button_clicks == 2:
        print('Please click the edge')
    elif button_clicks == 4:
        print('Please click the level start button')
    

def on_click_bbox(x, y, button, pressed):
    global clicks
    global word_palette_bbox

    clicks += 1

    if pressed:
        word_palette_bbox += (x, y)
        print(f'Pressed at {(x, y)}')

    if clicks >= 8:
        return False
    elif clicks == 2:
        print('Please click on the right of the word palette')
    elif clicks == 4:
        print('Please click on the bottom of the word palette')
    elif clicks == 6:
        print('Please click on the left of the word palette')


def on_release_key(key):
    if hasattr(key, 'char') and '-' == key.char:
        print('- Key Pressed, Terminating Program')
        os._exit(1)
        return False

def main():
    # Add a way to stop the loop
    listener = keyboard.Listener(
        on_release=on_release_key)
    listener.start()

    print('Please click the pig close')
    with mouse.Listener(
            on_click=on_click_buttons) as listener:
        listener.join()

    #print('Please click the level start button')
    #with mouse.Listener(
    #        on_click=on_click_level) as listener:
    #    listener.join()

    print('Please click on the top of the word palette')
    with mouse.Listener(
            on_click=on_click_bbox) as listener:
        listener.join()

    # Calculate the word palette bbox from the inputed points
    global word_palette_bbox
    _, y1, x2, _, _, y2, x1, _ = word_palette_bbox
    word_palette_bbox = (x1, y1, x2, y2)

    print('Piggy Close Pos:', piggy_close_pos)
    print('Edge Close Pos:', edge_close_pos)
    print('Level Button Pos:', level_button_pos)
    print('Word Palette BBox:', word_palette_bbox)

    # Get the cli arguments passed when the package was run
    args = sys.argv[1:]
    input_speed = 1
    for i in range(len(args)):
        if args[i] == '-s' or args[i] == '--speed':
            input_speed = float(args[i+1])

    wordscapes_bot = WordscapesBot(word_palette_bbox, level_button_pos, input_speed, piggy_close_pos, edge_close_pos)
    #wordscapes_bot = WordscapesBot(word_palette_bbox, level_button_pos, input_speed, piggy_close_pos)
    #wordscapes_bot = WordscapesBot(word_palette_bbox, level_button_pos, input_speed)
    wordscapes_bot.run()


if __name__ == "__main__":
    main()
