#homework 6-5,6-6
#6-5
rivers_and_countries = {"nile":"egypt","volga river:":"russia","ganges":"india"}
# print a sentence about each river
for rivers,country in rivers_and_countries.items():
    print(f"The {'nile'.title()} runs through {'egypt'.title()}.")
# print the name of each river
    #print(f"{'nile'.title()}.")
    print(f"{'volga river'.title()}.")
    print(f"{'ganges'.title()}.")
for river in rivers_and_countries:
#print(f"The {'volga river'.title()} runs through {'russia and europe'.title()}.")
# print the name of each country
#for country in rivers_and_countries.values():
    #print(f"The {'ganges'.title()} runs through {'india'.title()}.")
  # print(f"{'egypt'.title()}.")
   print(f"{'russia'.title()}")
   print(f"{'india'.title()}")

print("********************")

# H/W 6-6
favorite_languages = {'tom':'oracle','hamza':'python','lily':'sql'}
list_of_people_to_invite = {'tom','hamza','lily','kate'}
for person in list_of_people_to_invite:
    if person in favorite_languages:
     print(f"Thank you,{person.title()},for your respond!")
    else:
        print(f"Greetings {person.title()},You are invited to take your favorite computer languages!")



