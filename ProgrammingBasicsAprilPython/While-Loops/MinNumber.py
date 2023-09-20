import sys

command = input()
min_number = sys.maxsize # the initial number is a very large one we use to compare to the input number

while command != "Stop":
    current_number = int(command)
    if current_number < min_number:
        min_number = current_number
    command = input()
print(min_number)