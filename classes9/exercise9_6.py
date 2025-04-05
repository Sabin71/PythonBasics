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
class IceCreamStand(Restaurant):

    flavors= ['vanilla','chocolate','caramel','strawberry']

    def list_of_icecream_flavors(self):
        """
        :return: all available flavors"""
        for flavor in self.flavors:

           print(F"We have {flavor} ice-cream.")


ice_stand = IceCreamStand("Carvel",'american')
ice_stand.open_restaurant()
ice_stand.list_of_icecream_flavors()
ice_stand.describe_restaurant()
