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



