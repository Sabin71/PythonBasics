from classes9.cars import *

car1 = Car('lambo', 'huracan', 2025)

# instance has access to attributes and method
# car1 object can get values of attributes, execute functions, update values of attr.
car1.get_description()
# print(f"odometer reading: {car1.__odometer_reading}.")  # encapsulated
car1.__odometer_reading = 120

print("----------1 -------------")
car1.get_description()

# print(f"odometer reading: {car1.__odometer_reading}.") # encapsulated
car1.update_odometer(80)
# print(f"odometer reading: {car1.__odometer_reading}.") # encapsulated
car1.model = "Ferrari"
print("----------2 -------------")
car1.get_description()

# created the method to update the odometer
car1.update_odometer(70)
print("----------3 -------------")
car1.get_description()

car1.__odometer_reading = 90  # this is not right based on business logic. # encapsulated, does not work
print("----------4 -------------")
car1.get_description()


