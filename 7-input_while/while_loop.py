#while condition:
  # if above condition is true then execute code below
  # repeatable code here


#while True:
    #print('something') this is dangerous
# while 2>1:
# print('something else') dangerous

#increment a variable
num = 0
while num <5:
    print(f"current value of NUM : {num}")
    num = num + 1
print("---------------------")
num = 10
while num > 5:
    print(f"current value NUM : {num}")
    num = num -1
print("--------------------")

print("****************GAME STARTS !!! *********************")

total = 0
green_count = 0
alien_color = ""
while alien_color.lower() !='quit' and alien_color.lower() != 'q' :
    alien_color = input("Enter the color to earn points:")
    if alien_color.upper() =='GREEN':
      green_count += 1
    if green_count <= 1:
         total += 5 # increment -> total = total + 5
    else:
        total +=2
    print(f"You have just earned 5 points!\nTotal points:{total}")
    total =15
    print(f"You just earned 15 points.\nTotal points: {total}")
else:
    print("You just earned 10 points!\nTotal points: {total")
    yellow_count = 1

