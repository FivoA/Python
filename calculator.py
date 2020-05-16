print('Welcome to the calculator. \nPlease note that this programm is case sensitive and only accepts numbers for the number input!\n')
x = int(input('What is your first number?\n'))
y = int(input('What is your second number?\n'))
print('What would you like to do? ')
query = str(input('For an addition, type A. For a subtraction, type S, to multiply, type M and do divide, type D.\n'))
if query == 'A':
    sum = x + y
    print(sum)
elif query == 'S':
    sub = x - y
    print(sub)
elif query == 'M':
    mul = x * y
    print(mul)
elif query == 'D':
    div = x / y
    print(div)
else: 
    print('Sorry you entered an invalid keyword!')