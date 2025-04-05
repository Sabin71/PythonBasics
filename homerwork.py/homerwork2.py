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

print("__________________-")
#5-6,5-7
age = 20


if 2 > age > 0 :
    print(f"The person is a BABY")
elif 2 <= age < 4 :
     print (f"The person is a TODDLER")
elif 4 <= age < 13 :
    print(f"The person is a KID")
elif 13 <= age < 20 :
    print(f"The person is a TEENAGER")
elif 20 <= age < 65 :
    print (f"The person is an ADULT")
elif age >= 65 :
    print (f"The person is an ELDER")
else  :
    print (f"Please put valid age")

print("_______________________-")
#5-8
favorite_fruits = ['apples', 'bananas','kiwi']
if "apples" in favorite_fruits:
    print(f"You really like apples!")
if "bananas" in favorite_fruits:
    print(f" You really like bananas!")
if "kiwi" in favorite_fruits:
    print(f"You really like kiwi!")
if "grapes" in favorite_fruits:
    print(f"You really like grapes!")

print("-------------------------")
# 5 to 5=10
usernames = ["Eric", "Irine", "admin", "Bella", "Lola"]

for username in usernames:
    if username == "admin":
        print("Hello admin, would you like to see a status report?")
else:
        print(f"Hello {'Eric'}, thank you for logging in again!")
usernames = []
if usernames:
        print(f"hello_admin.py!")
else:
        print("We need to find some users!")
current_users = ["John","ela","sabina","leila", "frank"]
new_users = ["JOHN","sabina", "ela","kate","lisa"]
for new_user in new_users:

    if new_user.lower() in [user.lower()
for user in current_users]:
        print(f"Username'{new_user}' is already taken. Please choose a different one.")

else:
        print(f"Username'{new_users}' is available!")
print("#####################")

phrase = input("What is your plan for the summer break: ")
vowels_counts = {}

for letter in phrase.lower():
    vowels_counts.setdefault(letter, 0)
    vowels_counts[letter] += 5

print(vowels_counts)
