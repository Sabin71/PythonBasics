# Object-Oriented Programming concepts:
#Class,Object:
#Encapsulation - hiding the attribute ir method from instance (object),or hiding from the child:

class Car:
    """general car representation."""

    def __init__(self, make, model, year):
        """Constructor method of car class."""
        self.make = make
        self.model = model
        self.year = year
        # encapsulation with leading '__'
        self.__odometer_reading = 0  # attribute with default

    def get_description(self):
        print(f"Car details: {self.make}, {self.model.title()} {self.year}")
        print(f"with {self.__odometer_reading} miles on it.")

    def update_odometer(self, milage):
        # new value should not be less than existing value
        # new value => milage
        # existing vale => self.odometer_reading
        # when new value > existing then update to a new value
        # when new value <= existing then dont update, print a message
        if milage > self.__odometer_reading:
            self.__odometer_reading = milage
        else:
            print(f"Odometer can not be set less than {self.__odometer_reading}.")
    def get_odometer_reader(self):
        return self.__odometer_reading

class ElectricCar(Car) :
    """interitance of car class"""

    def __init__(self, make, model, year , battery_size = 85):
        """Constructor method of electric car class."""
        # call the constructor of parent

        super().__init__(make, model , year )
        #you cant pass batter_size because car class doesn't have this parameter)
        self.battery_size = battery_size
        #super refers to that car class(parent class)
        #you dont have to mention one more time self.make model year
        #self.make = make
        #self.model = model (those are overwriting)
        #self.year = year
        # encapsulation with leading '__'
        #self.__odometer_reading = 0


    def charge(self, kwh):
        print("Charging is initiated...")
        print(f"{self.model}charging reached intented kwd {kwh}")
        print(f"Your batter size is {self.battery_size}")
        # it is avaliable only electriccar (charge)

    #def get_description(self):
       # print("#####################")
        #print(f"Import Information about your electric car: ")
        #print(f"\n\tMake: {self.make.upper()}\n\tModel:{self.model.title()
       # }\n\tYear: {self.year}\n\tBattery size: {self.battery_size}")
        #print(f"Your current Odometer reading: {self.get_odometer_reading()}miles.")



