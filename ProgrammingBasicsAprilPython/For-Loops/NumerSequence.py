import sys #library
count_of_numbers = int(input())
max_number = -sys.maxsize #library sys, function maxsize returns a big number based on the number we input
min_number = sys.maxsize
for numbers in range(count_of_numbers):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    if current_number < min_number:
        min_number = current_number
print(f"Max number: {max_number}")
print(f" Min Number :{min_number}")