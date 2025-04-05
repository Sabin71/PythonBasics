def is_palindrome(phrase):
    reversed_phrase = ''
    for i in phrase:
        reversed_phrase = i + reversed_phrase
    return phrase.lower() == reversed_phrase.lower()



def is_palindrome2(phrase):
    ph_list = list(phrase)
    ph_list.reverse()
    return phrase == "".join(ph_list)


def is_palindrome3(phrase):
    return phrase == "".join(list(phrase)[:: -1])
print(is_palindrome3('kayak'))
print(is_palindrome3('hello'))
print(is_palindrome3('mom'))
   # for i in phrase:
        #reversed_phrase = i + reversed_phrase
   # return phrase.lower() == reversed_phrase.lower()

#print(list('hello'))
ph = list('hello')
print(ph)
print("".join(list('hello')[:: -1]))
