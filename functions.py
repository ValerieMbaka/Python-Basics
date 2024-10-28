# A block of code that performs a specific operation(s)
# Functions are reusable blocks of code that can be called multiple times

def add():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}")

add()

def square():
    num = int(input("Enter number: "))
    square = num ** 2
    print(square)
    # You can call a function within another function
    # add()

square()

def product(y):
    prd = y * y
    print(prd)

product(5)

def divide(x, y):
    print(f"{x} divided by {y} is {x / y}")
    # return x / y
    # pass

divide(10, 2)



