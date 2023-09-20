# cannot concatenate string and int/float , concatenation is for string
name = input()
print("Hello, " + name + "!")

# we use f" string formatting to concatenate text and a variable by casting the variable with curly brackets {}
print("Hello, ",
      end="")  # end = " " the end is the next row in the code, it will print the next block on the same row/
# we can add text within the quotes "" - it will add whatever is there before going to the next row
print(name, end="")
print("!")
