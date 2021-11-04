import json

dictionary = open('data.json')
words = json.load(words)

# Iterating through the json
# list
for i in words:
  print(i)

# Closing file
words.close()

dictionary = ["Hello", "Testing", "Testing", "hi", "hey", "hip"]

possibleWords = []
def dictTest(letters):
  for i in range(len(dictionary)):
    if(len(letters) >= len(dictionary[i]) && len(dictionary[i]) > 2):
      possibleWords.append(dictionary[i])

dictTest(["h", "e", "y"])
print(possibleWords)