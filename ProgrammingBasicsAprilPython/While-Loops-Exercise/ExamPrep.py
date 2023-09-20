END_COMMAND = "Enough"
UNDERSCORE = 4
total_grade = 0
count_grade = 0
last_problem_name = ""
count_not_good_grades = 0
not_good_grades_count = int(input())

while True:
    command = input()
    if command == END_COMMAND:
        break
    problem_name = command
    problem_grade = int(nput())
    total_grade += problem_grade
    count_grade += 1
    if problem_grade <= UNDERSCORE:
        count_not_good_grades += 1
        if count_not_good_grades >= not_good_grades_count:
            break
avg_grade = total_grade / count_grade
if command == END_COMMAND:
    print(f"Average score: {avg_grade}")
    print(f"Number of problems: {count_grade}")
    print(f"Last Problem: {problem_name}")
else:
    print(f"You need a break, {count_not_good_grades} poor grades")