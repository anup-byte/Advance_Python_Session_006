# class Attributes and Object Attributes

class Myclass1:
    class_attribute = "I am a class attribute"

# Creating the instances of the class

obj1 = Myclass1() 
obj2 = Myclass1() 

# Accessing Class attribute
print(obj1.class_attribute)
print()
print(obj2.class_attribute)
print()



# Instance Attribute

class Person:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age   # Instance attribute

# Creating the instances of the class

person1 = Person("Shanker", 40)
person2 = Person("Ruchi", 30)

# Accessing instance attribute
print(person1.name, person1.age)
print(person2.name, person2.age)

print()

# class and instance attributes

class Dog:
    # Class attribute shared by all instances
    species = "Labrador"

    def __init__(self, name, age):
        # Instance attributes unique to each instance
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


    


    # creating instances of the Dog class
dog1 = Dog("whisky", 3)
dog2 = Dog("Tommy", 15)   


    # Accessing the class attribute( Shared among all instances)
print(f"{dog1.name} belongs to the species {dog1.species}")
print(f"{dog2.name} belongs to the species {dog2.species}")

print()


print(dog1.description()) 
print(dog2.description())

print()

print(dog1.speak("Bark"))
print(dog2.speak("huuu"))

print()


            