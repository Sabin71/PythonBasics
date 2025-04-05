#execution and test scenerio
from modules_packages.customer_functions import get_customer_info
from modules_packages.customer_functions import update_customer_info
from modules_packages.customer_functions import delete_customer_info
from modules_packages.customer_functions import *
#import goes to customer file and execute them
#import executes the file when you have only definition in the file nothing will be in output
#(means everything inside customer_fun file I want to introduce)
#after from package name and file name whatever you want to import
#we have to put where it located starting from our project
#after import we can type one  function
#we are importing the definition because customer_function there is definition
# or you can do import get_customer, update_customer, delete_customer(in one line)
#BENEFITS:
print("#### 1. CREATE ###################")
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

