def add(a,b):
    return a+b
def calculator():
    operation = input('Enter the operation (+, -,*,/): ')
    num1 = float(input("First num: "))
    num2 = float(input("Second num: "))
    if operation =='+':
        result = add(num1,num2)

    print(result)

calculator()