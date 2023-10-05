numbers = input().split(' ')
remove = int(input())
numbers_as_integers = []
for current_number in numbers:
    numbers_as_integers.append(int(current_number))
    numbers_as_integers.sort(reverse=True)
for current_remove in range(remove):
    numbers.remove(str(numbers_as_integers.pop()))
print(', '.join(numbers))