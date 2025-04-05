num1 = 15
num2 = 22
# 1 swap using an extra variable
print(f"values of numbers,num1: {num1} and num2: {num2}")
#write code here
temp = num1
num1 = num2 #assign
num2 = temp
print(f"values of numbers,num1: {num1} and num2: {num2}")
print("_______________________________________")
# 2bswap without variable python way
num1,num2 = num2,num1
print(f"values of numbers,num1: {num1} and num2: {num2}")
print("--------------------------------------------")

print ("# 3 swap without variable(only with numbers).")
print(f"values of numbers,num1: {num1} and num2: {num2}")
num1 = num1 + num2 #15 +7 = 22
print(f"values of numbers,num1: {num1} and num2: {num2}")
num2 = num1 - num2 #22 -7 =15
print(f"values of numbers,num1: {num1} and num2: {num2}")
num1 = num1 - num2 # 22 - 15 =7
print(f"values of numbers,num1: {num1} and num2: {num2}")


