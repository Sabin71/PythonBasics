

while True:

  age = (input("Enter your age to see the ticket price:"))
  if age.lower() =='quit':
      print(f"Breaking the loop and exiting... ")
      break
  elif not age.isdigit():
      print(f"only positive numbers accepted. try again!!")
      continue
while True:

  age = int(input("Enter your age to see the ticket price:"))
  if age == 0:
      print(f"Breaking the loop and exiting... ")
      break
  if 0 < age <= 3:
      print(f"Ticket is Free for you!")
  elif 3 < age <= 12:
      print(f"Ticket price is $10.")
  elif age > 12:
      print(f"Ticket price is $15.")
  else:
      print(f"Please enter valid age. ")
      print("***************************8")
age = int(input("Enter your age to see the ticket price:"))

if 0 < age <= 3:
    print(f"Ticket is Free for you!")
elif 3 < age <= 12:
    print(f"Ticket price is $10.")
elif age > 12:
    print(f"Ticket price is $15.")
else:
    print(f"Please enter valid age. ")
print(f"Completed the excution of {__file__}.")