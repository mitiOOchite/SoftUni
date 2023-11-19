import re

sentence = input()
searched_word = input()
word = fr'\b{searched_word}\b'
count = len(re.findall(word, sentence, re.IGNORECASE))
print(count)
