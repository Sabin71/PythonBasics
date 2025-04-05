# unit testing:
# age = 'abc' --fail
#age =10 -- pass
# age = 17 -- pass
# age = None -- fail
# age =-10 ---> fail
age = 76 # -- pass
#age = 100
if 0 <= age  < 17:
    print("You are NOT eligable tp apply fpr Driver's permit.")
    print("You can apply after {17 - age} years.")
    # disable the continue button
elif age <= 17:
    print("You are eligable to apply for Driver's Permit.")
    #enable the continue button
elif age > 75:
    print("Ohh..Drive Carefully or just get an Uber/Lift.")
    print("make sure you renew the DL and drive carefully.")
else:
    print("please check the age entry, is not valid")
    # disable the continue button
print("------------------------------")





