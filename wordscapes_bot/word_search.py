import json

dictionary = open('data.json')
words = json.load(words)

# Iterating through the json
# list
for i in words:
  print(i)

# Closing file
words.close()

possibleWords = []
actualWords = []


def dict_test(letters):
    for i in range(len(dictionary)):
        if len(letters) >= len(dictionary[i]) > 2:
            possibleWords.append(dictionary[i])

    for i in range(len(possibleWords)):
        count = 0
        temp_letters = []
        for j in letters:
            temp_letters.append(j)
        for j in range(len(possibleWords[i])):
            if possibleWords[i][j].lower() in temp_letters:
                count += 1
                temp_letters.remove(possibleWords[i][j].lower())
        if count == len(possibleWords[i]):
            actualWords.append(possibleWords[i])


dict_test(["h", "e", "l", 'l', 'l', 'o'])
print(possibleWords)
print(actualWords)
