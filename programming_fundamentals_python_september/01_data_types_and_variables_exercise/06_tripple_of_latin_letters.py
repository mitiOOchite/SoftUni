number_of_symbols = int(input())

for first_symbol in range(number_of_symbols): #a
    for second_symbol in range(number_of_symbols):#a
        for third_symbol in range(number_of_symbols):#abc
            print(f'{chr(97+first_symbol)}{chr(97+second_symbol)}{chr(97+third_symbol)}')
