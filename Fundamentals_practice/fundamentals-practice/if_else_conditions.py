"""
Very Simple project demonstrating if and elif responses
"""
hey_bob = input("What would you like to ask? ")

def response(hey_bob):
    """
    This function takes an input strips it of un wanted whitespace and checks parameters of capitilization and ? to display how to respond.
    """
    hey_bob = hey_bob.strip()
    if not hey_bob:
        print ("Fine. Be that way!")
    elif hey_bob[-1] == "?" and hey_bob.isupper() == True:
        print ("Calm down, I know what I'm doing!")
    elif hey_bob[-1] == "?":
        print ("Sure.")
    elif hey_bob.isupper() == True:
        print ("Whoa, chill out!")
    else:
        print ("Whatever.")
    return (hey_bob)

response(hey_bob)
