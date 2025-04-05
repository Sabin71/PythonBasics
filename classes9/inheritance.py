
from classes9.cars import *
from classes9.cars import ElectricCar

#from classes9. Car, ElectricCar second option


#all attribute and methods are available to child
print("----regular car------")
car1 = Car('lambo', 'huracan', 2025)
car1.get_description()
car1.update_odometer(80)
car1.get_description()
#car1.charge #it is not available regular car it is only electricCar
#car1.get_odometer_reading()
car1.model = "abc"
print(car1.model)
#car1.get_describtion()

print("---------------electric car---------")
#it is still using the constructor of parent class
#everthing goes to original class

ecar1 = ElectricCar('tesla', 'sybertrack', 2025)
ecar1.get_description()
ecar1.update_odometer(80)
ecar1.get_description()
#print(ecar1.__odometer_reading) encapsulated
#you can access whatever is available in regular class
#you can't access encapsulated attributes

print(ecar1.make ,ecar1.model, ecar1.year)
ecar1.charge(10)

print("--------------")
ecar2 = ElectricCar('tesla', 'sybertrack', 2025, '75')
ecar2.get_description()
ecar2.update_odometer(200)
ecar2.get_description()
print(ecar2.make ,ecar2.model ,ecar2.year)
ecar2.charge(20)
