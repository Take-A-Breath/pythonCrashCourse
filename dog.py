class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting"""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over"""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
