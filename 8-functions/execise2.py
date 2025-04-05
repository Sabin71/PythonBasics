def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for letter in input_string.strip():
        # Add any non-blank letters to the
        # end of one string, and to the front
        # of the other string.
        new_string = new_string+letter.replace(" ","")
        reverse_string = letter.replace(" ","")+reverse_string
    # Compare
    if new_string.lower() == reverse_string.lower():
        return True
    return False

print(is_palindrome('mom')) # True
print(is_palindrome('hello')) # False
print(is_palindrome('kayak')) # True

print("*************************")
def is_palindrome(phrase):
    """
    Checks if a given phrase (only have letters) is a palindrome.
    Args:phrase: The string to check.
    Returns:True if the phrase is a palindrome, False otherwise.
    """
    # valid input  (only letters and at least 2 characters)
    if not phrase or not phrase.isalpha() or len(phrase) < 2: # "<:" --> lesss then
        return False
# Compare the phrase with its reverse
    return phrase == phrase[::-1] #--> " ::-" reverses a sequence(string,list,or tuple)
print(is_palindrome('mom'))  # True
print(is_palindrome('hello'))  # False
print(is_palindrome('kayak'))  # True



