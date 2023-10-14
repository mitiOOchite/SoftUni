def even_nums():
    numbers = input().split(', ')
    evens = [num for num in numbers if int(num) % 2 == 0]
    index_position = [i for i, num in enumerate(numbers) if int(num) %2 ==0] # enumerate returns the index and value, when we iterate through it i takes the index of the current number and num takes the actual value
    return index_position


print(even_nums())
