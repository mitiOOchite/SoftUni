input_line = input().split()  # Input is split into words

deciphered = []  # Initialize a list to store the deciphered words

for word in input_line:
    characters = []  # Initialize a list to store non-numeric characters
    numbers = ""  # Initialize a string to store numeric characters
    for x in word:
        if x.isnumeric():
            numbers += x
        else:
            characters.append(x)
    if numbers:
        ascii_letter = chr(int(numbers))  # Convert numeric characters to ASCII
        characters[0], characters[-1] = characters[-1], characters[0]  # Swap first and last characters
        ready_word = ascii_letter + ''.join(characters)  # Combine ASCII character with non-numeric characters
        deciphered.append(ready_word)  # Add the deciphered word to the list

output = ' '.join(deciphered)  # Join deciphered words with spaces

print(output)