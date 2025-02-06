# WordScapes Bot
![GitHub](https://img.shields.io/github/license/stelath/wordscapes-bot)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/stelath/wordscapes-bot)

A Python powered bot that solves WordScapes levels through OCR.

## Demo
![Demo Gif](https://i.giphy.com/media/1CyQXlFN6QcDLHU8Xu/giphy-downsized-large.gif)

## Setup
### Installing Tesseract
Download tesseract for Windows from UB-Mannheim:
https://github.com/UB-Mannheim/tesseract/wiki

OR, install for MacOS through Homebrew:
`
brew install tesseract
`

### Installing WordScapes Bot
Download a release from the release page then open your terminal and navigate to the folder the package was downloaded in; then run `pip install wordscapesbot-1.1.5.tar.gz` 

## Usage
Run the package by running `python -m wordscapesbot` in your terminal and following the instructuions that appear on the command line.

### Arguments
You can add arguments to the end of the expression ex. `python -m wordscapesbot (argument here)`
| Argument        | Description   |
| -------------   | :------------ |
| `-s or --speed` | Used to set the input speed, enter a float to change the speed (ex. `-s 2.5` inputs words 2.5 times faster)|

## Notice
This isn't designed to be a cheating device, but rather a fun engineering problem to solve and a fun thing to watch. Case in point, this is ironically the hard way to go about it. I'm sure if someone wanted to, they could just change the app data, as Wordscapes can be played offline and will still update the leaderboard online. This suggests they have no actual verification to ensure that points earned offline were earned legitimately. But that would be boring and there would be no real technical problem to solve. As to why I made this in the first place, to provide context, this project started as a joke with some friends who we're bragging about how they were better than me in Wordscapes. And since I'm dyslexic I wanted a funny way to get back at them so I made this.
