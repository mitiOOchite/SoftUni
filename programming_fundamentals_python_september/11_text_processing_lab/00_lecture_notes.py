# string = input()
# print(string[::-1])
# message = 'He said, "hello!"'
# print(message)
#
# print('I\'m happy')
#
# #isdigit() - check if a value is a digit
#
# data = input()
# digits = ''
# letters = ''
# for char in data:
#
#     if char.isdigit():
#         digits +=char
#     else:
#         letters+=char
# print(f'The user is {letters} and the number is {digits}')
import mysql.connector

cnx = mysql.connector.connect(user='root', password='NovaParola.2023',
                              host='127.0.0.1',
                              database='new')
cnx.close()