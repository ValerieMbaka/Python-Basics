class Animal:
        """
        This is a class that represents an animal
        """
        def __init__(self):
                self.name = input("Enter name: ")
                self.age = input("Enter age: ")
                self.sound = input("Enter sound: ")
                self.move = input("How do you move? ")

        def get_sound(self):
                return f"I am {self.name} and I produce {self.sound} sound"

        def get_move(self):
                return f"I {self.move} very fast"

animal = Animal()
print(animal.get_sound())
print(animal.get_move())
# print(f"Age: {animal.age}")
# print(f"Name: {animal.name}")
# print("---------------")

# print(animal)

# Inheritance - A class can inherit from another class
# Encapsulation - The bundling of data and the methods that operate on that data into a single unit
# Polymorphism - The ability of an object to take on many forms
# Abstraction - Hiding the complex implementation details of a class from the user


# Inheritance
class Dog(Animal):
        pass


print("-------------------------------------")
dog = Dog()
print(dog.get_sound())
print(dog.get_move())

class Cat(Animal):
        def get_sound(self):
                return "I produce meow sound"

animal = Animal("man", 12, "speak", "walk")
print(animal.get_sound())
print(animal.get_move())