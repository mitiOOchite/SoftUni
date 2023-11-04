keys = ['name','age','major']
values = ['Ivan','33','Computer Science']
student = {}

for i in range(len(keys)):
    key = keys[i]
    value = values[i]
    student[key] = value
old_name = student.get('name')
student['name'] = input('Please input the new name: ') #this is how we can change the value within the dict
print(f'{student}, \n The students old name was: {old_name}')