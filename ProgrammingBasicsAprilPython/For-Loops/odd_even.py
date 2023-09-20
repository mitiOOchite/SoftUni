count_of_numbers = int(input())
odd_sum = 0
even_sum = 0
for numbers in range(1, count_of_numbers + 1):
    current_number = int(input())
    if numbers % 2 == 0:
        odd_sum += current_number
    else:
        even_sum += current_number
if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    difference = abs(odd_sum - even_sum)
    print("No")
    print(f"Diff = {difference}")
