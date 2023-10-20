# {total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})
from math import ceil

number_of_students = int(input())
total_number_of_lectures = int(input())
additional_bonus = int(input()) + 5
total_bonus = 0
max_lectures = 0
for current_student in range(1, number_of_students + 1):
    student_attendance = int(input())
    current_bonus = (student_attendance / total_number_of_lectures) * additional_bonus
    if current_bonus > total_bonus:
        total_bonus = current_bonus
        max_lectures = student_attendance
print(f'Max Bonus: {ceil(total_bonus)}.')
print(f'The student has attended {max_lectures} lectures.')
