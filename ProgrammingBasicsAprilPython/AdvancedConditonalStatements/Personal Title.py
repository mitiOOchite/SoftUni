age = float(input())
gender = input()

if gender == "m":
    if age >= 16:
        title = "Mr."
    else:
        title = "Master"
elif  gender == "f":
    if age >= 16:
        title = "Mrs."
    else:
        title = "Missis"
print(title)
