customer1 = {
      "CustomerID": "ALFKI",
      "CompanyName": "Alfreds Futterkiste",
      "ContactName": "Mania Anders",
      "ContactTitle": "Sales Representative",
      "Address": "Obore Str. 57",
      "City": "Berlin"
      "Region" "None",
      "PostalCode": 12209,
      "Country": "Germany",
      "Phone": "030-0074321",
      "Fax": "030-0076545",
}


print("# by Default for looping in dictionary it returns only KEY")
for column in customer1:
    print(f"column name: {column}")

print("----------")
print(" # 1. Loop through each Element (key,value.")
for column, value in customer1.items():
    print(f"column name: {column}")
    print(f"column value: {value}")
    print("*******************************")

for key, value in customer1.items():
    print(f"column name: {key}")
    print(f"column value: {value}")
    print("*******************************")

print(" # 2. Loop through key only")
print(" # Default,for loop in dictionary returns onlu keys")
for column in customer1:
    print(f"column name: {column}")

print("--------------------")
print("# using keys(),for loop in dictionary returns only key")
for key in customer1.keys():
    print(f"column name: {key}")
    print(f"column value: {customer1[key]}")

print("##################################")
print("# 3. Loop through Value only")
print("# for loop in dictionary returns only values")
for value in customer1.values():
    print(f"column value: {value}")

columns = list(customer1.keys())
print()

#Loop through each Element (key,value)
#Loop through key only
#Loop through Values only
