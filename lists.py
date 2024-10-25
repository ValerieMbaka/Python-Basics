students =["Val", "Joy", "Sam", "Hyke"]
print(students)

# Counting the number of items in a list
# Use the len() function
print(len(students))

# Accessing list items
print(students[0])

# Print the last item in the tuple
print(students[-1])

# Printing a range of items in the list
print(students[:3])  # Prints items up to index 2, the third index is ignored

print(students[1:3]) # Prints items from index 1 to index 2
print(students[-1:-3])  # Prints nothing because the range is invalid
print(students[-3:-1])  # Prints items from the third last index to the second last index


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

# Changing the value of an index
students[0] = "Faith"