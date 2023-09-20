text = input()
sum_points = 0
for symbol in text:
    if symbol == "a":
        sum_points += 1
    elif symbol == "e":
        sum_points += 2
    elif symbol == "i":
        sum_points += 3
    elif symbol == "o":
        sum_points += 4
    elif symbol == "u":
        sum_points += 5
print(sum_points)
