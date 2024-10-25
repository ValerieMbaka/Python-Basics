students =["Val", "Joy", "Sam", "Hyke"]
print(students)

# Counting the number of items in a list
# Use the len() function
print(len(students))

# Accessing list items
print(students[0])

# Write a program to print out the specific index of the last item in a list
index = len(students) - 1
print(index)

# Adding items to a list
# insert() requires one to specify the specific index that the item is to be added
students.insert(1, "Yvonne")

# append() adds the item to the end of the list
students.append("Pauline")


# Removing items from a list
# remove()
students.remove("Hyke")