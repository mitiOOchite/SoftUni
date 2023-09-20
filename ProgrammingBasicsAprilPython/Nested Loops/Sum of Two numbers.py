start = int(input())
final = int(input())
magic_number = int(input())
combination_is_found = False
count = 0

for first_number in range(start, final+1):
    for second_number in range(start, final+1):
        count += 1
        if first_number+second_number == magic_number:
            combination_is_found = True
            break
    if combination_is_found:
        break
if combination_is_found:
    print(f"Combination: N{count} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{count} combinations")