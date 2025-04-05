'''
DICTIONARY (HASHMAP)
A dictionary in Python is a collection of key-value pairs. Each key is connected
to a value, and you can use a key to access the value associated with that key.
A key’s value can be a number, a string, a list, or even another dictionary.
'''

customer1 = {
    "CustomerID": "ALFKI",
    "CompanyName": "Alfreds Futterkiste",
    "ContactName": "Maria Anders",
    "ContactTitle": "Sales Representative",
    "Address": "Obere Str. 57",
    "City": "Berlin",
    "Region": None,
    "PostalCode": 12209,
    "Country": "Germany",
    "Phone": "030-0074321",
    "Fax": "030-0076545",
}
customer2 =   {
    "CustomerID": "ANATR",
    "CompanyName": "Ana Trujillo Emparedados y helados",
    "ContactName": "Ana Trujillo",
    "ContactTitle": "Owner",
    "Address": "Avda. de la Constitución 2222",
    "City": "México D.F.",
    "Region": None,
    "PostalCode": "05021",
    "Country": "Mexico",
    "Phone": "(5) 555-4729",
    "Fax": "(5) 555-3745"
}
customer3 = dict()

print("#### 1. CREATE ###################")
def get_customer_info(customer):
    '''
    Prints Important Customer information from the input dictionary
    :param customer: it should be dictionary containing customer information
    :return:
    '''
    # print(customer)

    print("#### 2. READ (ACCESS THE VALUES) ###################")
    print(f"*** Here is the Information about : {customer['CompanyName']} ********")
    print(f"ID of the customer: {customer['CustomerID']}")
    print(f"The customer is located in: {customer['Country'].upper()}")
    print(f"Country - using get() function: {customer.get('Country')}")


def update_customer_info(customer, new_city, is_active):
    print("#### 3. UPDATE ###################")
    customer.setdefault('City', None)
    print(f"The customer city before update: {customer['City']}")
    customer['City'] = new_city
    print(f"The customer city after update: {customer['City']}")
    # print(customer)

    print("Setdefault for isActive (first) ...........")
    existing_value = customer.setdefault("isActive", False)
    print(f"Existing value of the isActive : {existing_value}")
    # print(customer)

    print("Adding new info - key-value pair ....")
    customer["isActive"] = is_active

    # print(customer)
    print("Setdefault for isActive (second) ...........")
    existing_value = customer.setdefault("isActive", False)
    print(f"Existing value of the isActive : {existing_value}")
    print(customer)


def delete_customer_info(customer, key):
    print("#### 4. DELETE ###################")
    print(customer)
    removed_info = customer.pop(key)  # returns the value removed
    print(customer)
    print(f"Removed '{key}' from customer: {removed_info}")
    return removed_info


get_customer_info(customer1)
update_customer_info(customer1, 'Frankfurt', True)
get_customer_info(customer1)

get_customer_info(customer2)
# read_customer_dictionary(customer3) # KeyError: 'CompanyName'

update_customer_info(customer3, 'Paris', True)


# errormssage = delete_customer_info(customer1, 'Fax')
# assert errormssage == "sorry you can .."  # verifying the correct error message
exp_fax = "030-0076545"

deleted_fax = delete_customer_info(customer1, 'Fax')
print(f"Is it deleted correct value: {deleted_fax == exp_fax}")
assert deleted_fax == exp_fax  # pass and fail control in python code

delete_customer_info(customer1, 'Phone')
delete_customer_info(customer1, 'Region')




