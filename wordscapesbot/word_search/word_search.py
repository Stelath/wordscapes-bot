import json
import os


def word_search(letters, short_dict=True):
    script_dir = os.path.dirname(__file__)
    rel_path = 'words_dictionary_short.json' if short_dict else 'words_dictionary_long.json'
    abs_file_path = os.path.join(script_dir, rel_path)

    words = open(abs_file_path, 'r')
    dictionary = json.load(words)

    possible_words = []
    actual_words = []

    for word in dictionary:
        if len(letters) >= len(word) > 2:
            possible_words.append(word)

    for i in range(len(possible_words)):
        count = 0
        temp_letters = letters.copy()
        for j in range(len(possible_words[i])):
            if possible_words[i][j].lower() in temp_letters:
                count += 1
                temp_letters.remove(possible_words[i][j].lower())
        if count == len(possible_words[i]):
            actual_words.append(possible_words[i])

    # Closing file
    words.close()

    return actual_words
