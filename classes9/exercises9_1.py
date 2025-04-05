class Restaurant:

 """ A class represent general restaurant."""

 def __init__(self,restaurant_name,cuisine_type):
        """This is a Constructor of the class."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
 def describe_restaurant(self):
     print(f" This is {self.restaurant_name.title()} is fine {self.cuisine_type.upper()} cuisine. >>> ")

 def open_restaurant(self):
     print(f" *** Welcome to {self.restaurant_name.upper()}! We are open!")


restaurant1 = Restaurant('Bella napoli','italian')
restaurant1.open_restaurant()
restaurant1.describe_restaurant()

print("---------9-2--------------")
restaurant2 = Restaurant('egg harbour','american')
restaurant2.open_restaurant()
restaurant2.describe_restaurant()

restaurant3 = Restaurant('cote brasserie','french')
restaurant3.open_restaurant()
restaurant3.describe_restaurant()
