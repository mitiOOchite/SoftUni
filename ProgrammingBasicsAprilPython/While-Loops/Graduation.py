student_name = input()
bad_tries = 0
current_class = 1
total_grade = 0

while current_class <= 12:
    current_grade = float(input())
    if current_grade < 4:
        bad_tries += 1
        if bad_tries > 1:
            break
        continue
    current_class += 1
    total_grade += current_grade
if current_class <= 12:
    print(f"{student_name} has been excluded at {current_class} grade")
else:
    average_grade = total_grade/12
