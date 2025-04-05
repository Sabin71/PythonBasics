def greet_user():
    print("Hello!")


def greet_user_by_name(user_name):
    print(f"Hello,{user_name.title()}!")


def describe_pet(animal_type,pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
greet_user()
greet_user_by_name('john')
greet_user_by_name('jane')
greet_user_by_name('lili')

#print("today",'is Sunday',2+2, 'is 5',False)
#print("today",'is Sunday', 2+2,'is 5', False, sep="|",end="<3@@@")
#print("aabb")

print("*******positional argument **********")
describe_pet('horse', 'maximus')

describe_pet(animal_type='dog', pet_name= 'mol')

print("************keyword argument ***************")
describe_pet(pet_name='maximus',animal_type='horse')
#h/w 8-3 till 8-5
