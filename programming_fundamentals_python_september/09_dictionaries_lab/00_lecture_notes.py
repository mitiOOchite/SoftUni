# keys = ['name','age','major']
# values = ['Ivan','33','Computer Science']
# student = {}
#
# for i in range(len(keys)):
#     key = keys[i]
#     value = values[i]
#     student[key] = value
# old_name = student.get('name')
# student['name'] = input('Please input the new name: ') #this is how we can change the value within the dict
# print(f'{student}, \n The students old name was: {old_name}')

student_records = {
    "Ivan":{"Math":5,"Science":6,"English":5},
    "Mitko":{"Math":4,"Science":3,"English":2},
    "Nikolay":{"Math":4,"Science":3,"English":2},
}
for name, value in student_records.items():
    print(f'*** {name} ***')
    for subject,score in value.items():
        print(f'{subject} - {score}')