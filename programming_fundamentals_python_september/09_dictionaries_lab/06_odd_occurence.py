elements = input().split()
element_dict = {}
for word in elements:
    lowercase_word = word.lower()
    if lowercase_word not in element_dict:
        element_dict[lowercase_word] = 0
    element_dict[lowercase_word] += 1
for key, value in element_dict.items():
    if value%2 != 0:
        print(key, end = " ")