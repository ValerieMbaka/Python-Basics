# If statements
# math = 72
# english = 56
#
# if math < english:
#     print("Maths is less than English")
#
# elif math > english:
#     print("Maths is greater than English")
#
# else:
#     print("Maths is equal to English")

# A python program that checks whether a number is positive, negative or zero
# y = int(input("Enter a number: "))
# if y > 0:
#     print(f"{y} is positive")
# elif y < 0:
#     print(f"{y} is negative")
# else:
#     print(f"{y} is zero")

# Checks whether the number is odd or even
# if y % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# A program that calculates the square of any given value
# num = int(input("Enter a number: "))
# square = num ** 2
# print(square)


# Grading system
# 0 - 39 D
# 40 - 59 C
# 60 - 79 B
# 80 - 100 A


# maths = int(input("Enter marks for Maths: "))
# if maths < 0 or maths > 100:
#     print("Invalid marks!")

# eng = int(input("Enter marks for English: "))
# if eng < 0 or eng > 100:
#     print("Invalid marks!")

# kis = int(input("Enter marks for Kiswahili: "))
# if kis < 0 or kis > 100:
#     print("Invalid marks!")

# geo = int(input("Enter marks for Geography: "))
# if geo < 0 or geo > 100:
#     print("Invalid marks!")

maths = 60
eng = 75
kis = 89
geo = 66

total = maths + eng + kis + geo
print(f"Total marks: {total}")
avg = total / 4
print(f"Average marks: {avg}")

if 80 <= avg >= 100:
    print("A")
elif avg >= 60:
    print("B")
elif avg >= 40:
    print("C")
elif 39 >= avg >= 0:
    print("D")
else:
    print("Invalid")