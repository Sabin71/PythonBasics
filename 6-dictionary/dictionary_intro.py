print("### 1. CREAT #########")
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

customer2 = {}
customer3 = dict()
print(customer1)


print("#### 2. READ (ACCESS THE VALUES) ##########")
print(f"ID of the customer: { customer1['CustomerID'] }")
print(f"name of the customer: { customer1['CompanyName'] }")
print(f"The customer is located in: {  customer1 ['Country'] .upper()}")


print("#### 3. UPDATE ##############")
print(f"The customer city before update: { customer1['City']  }")
customer1['City'] = "Frankfurt"
print(f"The customer city after update: {  customer1['City'] }")
print(customer1)

print("Adding new info - key-value pair  .... ")
customer1["isActive"] = True

print(customer1)
print("Setdefault for is Active ........")
existing_value = customer1.setdefault("isActive", False)
print(f"Existing value of the isActive: {existing_value}")
print(customer1)

existing_value2 = customer2.setdefault("isActive",False)
print(f"Exsisting value of the isActive for customer2: {existing_value2}")
print(customer2)

print("#### 4. DELETE #############")
del customer1["Fax"]
print(customer1)
removed_info = "customer1.pop ('Phone') : {removed_info}"



