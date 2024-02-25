
# Online Python - IDE, Editor, Compiler, Interpreter


num_one = int(input('What is your first number?'))
num_two = int(input('What is the second number?'))
operation = input('What operation would you like to complete?')
if operation == '+':
    print(num_one + num_two)
elif operation == '-':
    print(num_one + num_two)
elif operation == '*':
    print(num_one * num_two)
elif operation == '/':
    if num_two != 0:
         print(num_one / num_two)
    else:
        print("cannot divide by zero")
else:
    print("Invalid ")