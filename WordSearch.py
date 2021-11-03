dictionary = ["Hello", "Testing", "Testing", "hi", "hey", "hip"]

possibleWords = []
def dictTest(letters):
  for i in range(len(dictionary)):
    if(len(letters) >= len(dictionary[i]) && len(dictionary[i]) > 2):
      possibleWords.append(dictionary[i])

dictTest(["h", "e", "y"])
print(possibleWords)