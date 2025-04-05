import yaml
from utilities import read_yaml_file

customers_path = "./data/customer.yml"

with open(customers_path, 'r') as file:
    customers = yaml.safe_load(file)

print(customers['customer1']['CompanyName'])

print(customers['customer1']['Region'])
print(customers['customer1']['PostalCode'])
print(customers['customer1']['PhoneNumbers'])
print(customers['customer1']['PhoneNumbers'][0])

print("-------------------------------------")
config_path = ('./data/config.yml')
config = read_yaml_file(config_path) # dictionary

# print(f"link for dev env: {config['DEV']['url']}")
# print(f"username for dev env: {config['DEV']['username']}")
# print(f"password for dev env: {config['DEV']['password']}")

env = 'QA'  # [DEV, QA]
for env in ['DEV', 'QA']:
    url = config[env]['url']
    user_name = config[env]['username']
    pword = config[env]['password']

    print(f"Open the website : {url}")
    print(f"enter username '{user_name}'")
    print(f"enter the password '{pword}'")
    print("Click on Sign in button ...")