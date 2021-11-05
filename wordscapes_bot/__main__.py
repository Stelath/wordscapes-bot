import pytesseract.pytesseract
from pynput import mouse
from wordscapes_bot.wordscapes_bot import WordscapesBot


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


def main():
    with mouse.Listener(
            on_click=on_click) as listener:
        listener.join()

    print(word_palette_bbox)
    wordscapes_bot = WordscapesBot(word_palette_bbox)
    wordscapes_bot.run()

if __name__ == "__main__":
    main()
