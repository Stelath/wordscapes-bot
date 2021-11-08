import time
from wordscapesbot.word_search import word_search

start_time = time.time()
test_one = word_search(['h', 'e', 'l', 'l', 'o'])
end_time = time.time()
print(f'Word search 1 took {end_time - start_time} seconds')

start_time = time.time()
test_two = word_search(['g', 'p', 'i', 't', 'u', 't', 'h'])
end_time = time.time()
print(f'Word search 2 took {end_time - start_time} seconds')

print('Test 1:')
print(test_one)

print('Test 2:')
print(test_two)
