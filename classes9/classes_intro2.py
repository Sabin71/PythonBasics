class Dog:
    """General representation of real world dog"""

    #attribute
    #rewrite the constructor
    def __init__(self,name,age):
     self.name = name
     self.age = age

    # behavior
    def sit(self):
        print(f"{self.name} is sitting.")

    def roll_over(self):
      print(f"{self.name} is rolling over {self.age} times because it is {self.age}years old.")
 # creating the object - instantiation
my_dog = Dog('Willie',  2) # my_dog is the object
my_dog.sit()

friend_dog = Dog('Roksi',  4) # assigning new value name and attribute

friend_dog.sit()
my_dog.sit ()
my_dog.roll_over()
friend_dog.roll_over()

my_dog.age = 4
my_dog.roll_over()

my_dog.name = 'Charlie'
my_dog.roll_over()
