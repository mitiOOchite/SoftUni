# filename_and_extension = input().split("\\")
# for file in range(len(filename_and_extension)-1, len(filename_and_extension)):
#     filename, extension = filename_and_extension[file].split('.')
# print(f'File name: {filename}')
# print(f'File extension: {extension}')

filename_and_extension = input().split("\\")
file = filename_and_extension[-1]
filename,extension = file.split('.')
print(f'File name: {filename}')
print(f'File extension: {extension}')