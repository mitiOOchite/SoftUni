command = input()
course_dict = {}
while command != 'end':
    course_name, student = command.split(" : ")
    if course_name in course_dict:
        course_dict[course_name].append(student)
    else:
        course_dict[course_name] = [student]
    command = input()
for key, value in course_dict.items():
    print(f'{key}: {len(value)}')
    for current_attendee in value:
        print(f'-- {current_attendee}')
