import json
import os

script_dir = os.path.dirname(__file__)
rel_path = "words_dictionary.json"
abs_file_path = os.path.join(script_dir, rel_path)

words = open(abs_file_path, 'r')
dictionary = json.load(words)

def word_search(letters):
    possible_words = []
    actual_words = []

    for word in dictionary:
        if len(letters) >= len(word) > 2:
            possible_words.append(word)

    for i in range(len(possible_words)):
        count = 0
        temp_letters = []
        for j in letters:
            temp_letters.append(j)
        for j in range(len(possible_words[i])):
            if possible_words[i][j].lower() in temp_letters:
                count += 1
                temp_letters.remove(possible_words[i][j].lower())
        if count == len(possible_words[i]):
            actual_words.append(possible_words[i])

    return actual_words

# Closing file
words.close()