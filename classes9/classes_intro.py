class Dog:
    """General representation of real world dog"""

    #attribute
    name = 'Wallie'
    age = 2

    # behavior
    def sit(self):
        print(f"{self.name} is sitting.")

    def roll_over(self):
      print(f"{self.name} is rolling over {self.age} times because it is {self.age}years old.")
 # creating the object - instantiation
my_dog = Dog() # my_dog is the object
my_dog.sit()

friend_dog = Dog()
friend_dog.name = 'Roksi' # assigning new value name and attribute
friend_dog.age = 3
friend_dog.sit()
my_dog.sit ()
my_dog.roll_over()
friend_dog.roll_over()
