for i in range(1, 10): #i<= 12 the range is always the number before and starts from the begining
    print(i)
for i in range(1, 10, 2): #when we have a 3rd argument we have a step for the loop range(start, final, step)
    i += 100
#we can do calculation with the step from the for loop, we do not change it with this statement,
#we add its value
#for loop works only with whole numbers
    print(i)
# the syntaxis can be either (start. final, step) or (start, final) or just (final)
for i in range(10, 1, -1): #i<= 12 the range is always the number before and starts from the begining
    print(i)

some_string = "text"
text_len = len(some_string)
print(text_len)
print(some_string[0])
print(some_string[1])
print(some_string[2])
print(some_string[3])
print(some_string[-1])
print(some_string[-2])
print(some_string[-3])
print(some_string[-4])
# we can go from the end to the start
#taking the length of the text
#text val------------->  t e x t
#indexing numbers -->    0 1 2 3 indexing starts from 0 we use brackets to get the index value []
for index in range(text_len):
    print(f"Index = {index} symbol = {some_string[index]}")
for character in some_string: #we can use character it creates something like an index on the back and prints the chars
    print(character)
for index, character in enumerate(some_string):
    print(f"Index = {index}, symbol = {character}")
