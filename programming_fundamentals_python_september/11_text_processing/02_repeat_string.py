# word = input().split()
# new_word = ''
# for char in word:
#     new_word += char*len(char)
# print(new_word)

word = input().split()
new_word = [char*len(char) for char in word]
print("".join(new_word))