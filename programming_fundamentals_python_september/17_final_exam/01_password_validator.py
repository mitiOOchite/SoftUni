import re
password = input()
password_list = list(password)
command = input()
while command != 'Complete':
    if ' ' in command and len(command.split(' ')) == 3:
        action, value, char = command.split(' ')
        if action == 'Make':
            if value == "Upper" and 0 <= int(char) < len(password_list):
                password_list[int(char)] = password_list[int(char)].upper()
                print(''.join(password_list))
            elif value == "Lower" and 0 <= int(char) < len(password_list):
                password_list[int(char)] = password_list[int(char)].lower()
                print(''.join(password_list))
        elif action == "Insert" and 0 <= int(value) <= len(password_list):
            password_list.insert(int(value),char)
            print(''.join(password_list))
        elif action == 'Replace' and value in password_list:
            new_value = chr(ord(value)+int(char))
            string_pass = ''.join(password_list)
            password_list = list(string_pass.replace(value,new_value))
            print(''.join(password_list))
    elif command == 'Validation':
        pass_string = ''.join(password_list)
        if len(pass_string) <8:
            print("Password must be at least 8 characters long!")
        if not re.search(r'^[a-zA-Z0-9_]+$',pass_string):
            print("Password must consist only of letters, digits and _!")
        if not re.search(r"[A-Z]{1,}", pass_string):
            print("Password must consist at least one uppercase letter!")
        if not re.search(r'[a-z]{1,}',pass_string):
            print("Password must consist at least one lowercase letter!")
        if not re.search(r'\d{1,}',pass_string):
            print("Password must consist at least one digit!")
    command = input()
