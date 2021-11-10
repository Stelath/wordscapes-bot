# WordScapes Bot
![GitHub](https://img.shields.io/github/license/stelath/wordscapes-bot)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/stelath/wordscapes-bot)

A Python powered bot that solves WordScapes levels through OCR.

## Setup
### Installing Tesseract
Download tesseract for Windows from UB-Mannheim:
https://github.com/UB-Mannheim/tesseract/wiki

OR, install for MacOS through Homebrew:
`
brew install tesseract
`

### Installing WordScapes Bot
Download a release from the release page then open your terminal and navigate to the folder the package was downloaded in; then run `pip install wordscapesbot-1.1.0.tar.gz` 

## Usage
Run the package by running `python -m wordscapesbot` in your terminal

### Arguments
You can add arguments to the end of the expression ex. `python -m wordscapesbot (argument here)`
| Argument       | Description   |
| -------------  | :------------ |
| -s or --speed  | Used to set the input speed, enter a float to change the speed (ex. `-s 2.5` inputs words 2.5 times faster)|
