print("********* Print odd number from 1 to 20.**********")
for num in range(1,21,2):
    print(num)

print("********** A list of the multiples of 3 from 3 to 30.*********")
for num in range(3, 31, 3):
    print(num)



list_numbers = []
for list_numbers in range(1,1):
    print(list_numbers)


list_numbers = list(range (1,10))



my_pizzas = ["Margherita","Veggie pie","Cheese pie"]
friend_pizzas = my_pizzas[:]
my_pizzas.append('thin crust')
friend_pizzas.append('more cheese')
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

print("-------------------------------")
#grren alien/ 5--4,5-5

green = 5
yellow = 10
red = 15
for i in  range (5):
    green_count = 5
if green_count == 5:
    print("You just earned 5 points for shooting the green alien!")
else:
    print("You just earned 10 points !")
#non green alien
alien_color ='red'
if alien_color == 'green':
    print("You just earned 5 points for shooting the green alien!")
else:
    print("You just earned 10 points!")
alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 15 points!")

