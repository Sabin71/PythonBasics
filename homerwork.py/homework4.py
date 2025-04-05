
#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
#text of a message that should be printed on the shirt. The function should print
#a sentence summarizing the size of the shirt and the message printed on it.
#Call the function once using positional arguments to make a shirt. Call the
#function a second time using keyword arguments.



#positional arguments
def make_shirt(size,message):
    print(f"{size} : The chest is 18.5 inch and body length 23.5 inches")
    print(f"{message} : It comes small, purchase one size bigger")
make_shirt('Small' ,'Suggestion' )

#keyword arguments
def make_shirt(size,message):
    print(f"{size} : The chest is 18.5 inch and body length 23.5 inches")
    print(f"{message} : It comes small, purchase one size bigger")
make_shirt(message= 'Suggestion' , size= 'Small') #we can add another parameter\argument here (optional)

#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
#by default with a message that reads I love Python. Make a large shirt and a
#medium shirt with the default message, and a shirt of any size with a different
#message.

def make_shirt(message , size='Large'):
    print(f"{size} : The chest is 25 inch and body length 30 inches")
    print(f"I love {message}!")
make_shirt(message = 'Pyton')
def make_shirt(size='large', message='I love Python'):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f"It will say, \"{message}\"")

# Call the function using positional arguments
make_shirt('medium', 'I love Python!')

# Call the function using keyword arguments
make_shirt(size='small', message=' WoW Python!')

# Large shirt with default message
make_shirt()

# Medium shirt with default message
make_shirt(size='medium')

# Small shirt with a different message
make_shirt(size='small', message='Code for life,!')
print("************************")
#8-5
def describe_city(city,country = 'Iseland'):
  """Prints a simple sentence ."""
  print(city.title() + " is in " + country.title() + ".")

# function for three different cities
describe_city('reykjavik')
describe_city('cairo', 'egypt')
describe_city('tashkent', 'uzbekistan')
describe_city('miami','usa')






