grade_count = int(input())
student_dict = {}
count = 0
for _ in range(grade_count):
    student = input()
    grade = float(input())
    if student in student_dict:
        count+=1
        student_dict[student].append(grade)
    else:
        student_dict[student] = [grade]
for key,value in student_dict.items():
    if sum(value)/len(value) >=4.50:
        print(f'{key} -> {sum(value)/len(value):.2f}')