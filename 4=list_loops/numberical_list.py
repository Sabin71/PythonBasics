print(list(range(10)))

for num in range(10):
    print(num)
print("--------------------")
#how do you loop only 3 times?
for num in range(3):
    print(num)
print("**********how do you print even numbers from 20 to 30 **********?")
for num in range(20,31,2):
    print(num)

print("*********Print numbers dividable by 5 between 60 and 93? *****")
for num in range(60,93,5):
    print (num)

print("*********Print square of numbers between 160 and 171? *****")
for num in range(160,171):
    print (f"Square of{num} is {num**2}.")


print("*********Print cube of numbers between 160 and 171? *****")
for num in range(160,171):
    print (f"Cube of{num} is {num**3}.")


print("*********Print cube of numbers between 160 and 171.Do not print individual numbers *****")
cubes = []
for num in range(160,171):
    cubes.append(num**3)
print(f"Cubes of the numbers: {cubes}")

print("*********Print sum  of numbers between 160 and 171.Do not print individual numbers *****")
sum = 0
for num in range(160,171):
    print(f"num is {num}")
    print(f"sum is {sum}")
    sum+=num
    print("**************")
print(f"RESULT: {sum}")



print("********* Print odd number from 1 to 20.**********")
for num in range(1,21,2):
    print(num)

print("********** A list of the multiples of 3 from 3 to 30.*********")
for num in range(3,31,3):
    print(num)
