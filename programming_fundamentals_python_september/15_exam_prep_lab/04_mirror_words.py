import re

data = input()
pattern = r'(#|@)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})\1'
result = re.findall(pattern, data)
mirror_words = []
the_count_of_words = len(result)
if result:
    for pair in result:
        if pair[1] == pair[3][::-1]:
            mirror_words.append(f'{pair[1]} <=> {pair[3]}')
    print(f'{the_count_of_words} word pairs found!')
else:
    print('No word pairs found!')
if len(mirror_words) > 0:
    print('The mirror words are:')
    print(', '.join(mirror_words))
else:
    print("No mirror words!")