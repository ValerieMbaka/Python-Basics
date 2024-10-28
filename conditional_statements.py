# If statements
math = 72
english = 56

if math < english:
    print("Maths is less than English")

elif math > english:
    print("Maths is greater than English")

else:
    print("Maths is equal to English")

# A python program that checks whether a number is positive, negative or zero
y = int(input("Enter a number: "))
if y > 0:
    print(f"{y} is positive")
elif y < 0:
    print(f"{y} is negative")
else:
    print(f"{y} is zero")

# Checks whether the number is odd or even
if y % 2 == 0:
    print("Even")
else:
    print("Odd")

# A program that calculates the square of any given value
num = int(input("Enter a number: "))
square = num ** 2
print(square)


# Grading system
# 0 - 39 D
# 40 - 59 C
# 60 - 79 B
# 80 - 100 A

maths = 60
eng = 76
kis = 89
geo = 66

total = maths + eng + kis + geo
avg = total / 4

if avg >= 80:
    print("A")
elif avg >= 60:
    print("B")
elif avg >= 40:
    print("C")
else:
    print("D")
