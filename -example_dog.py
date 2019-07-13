## https://realpython.com/python3-object-oriented-programming/

class Dog:

    # Class Attribute
    species = 'mammal'
    year = 2019

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.birth = self.year - self.age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

# Access the instance attributes
print("{} is {} and {} is {}.".format(
    philo.name, philo.age, mikey.name, mikey.age))

# call our instance methods
print(mikey.description())
print(mikey.speak("Gruff Gruff"))

print("{} is born in {}".format(
    philo.name, philo.birth))
