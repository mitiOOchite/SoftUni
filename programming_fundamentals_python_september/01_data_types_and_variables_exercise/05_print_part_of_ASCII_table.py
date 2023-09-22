char_index1 = int(input())
char_index2 = int(input())
for asci in range(char_index1, char_index2 + 1):
    if asci == char_index2:
        print(chr(asci))
    else:
        print(chr(asci), end=' ')
