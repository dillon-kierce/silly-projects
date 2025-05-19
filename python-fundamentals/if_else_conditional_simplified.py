"""
Simplified Simple project demonstrating if and elif responses
"""
hey_bob = input("What would you like to ask? ")

def response(hey_bob):
    """
    This function takes an input strips it of un wanted whitespace and checks parameters of capitilization and ? to display how to respond.
    """
    hey_bob = hey_bob.strip()
def response(hey_bob):
    hey_bob = hey_bob.strip()
    
    if not hey_bob:
        return 'Fine. Be that way!'
    elif hey_bob[-1] == '?':
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return 'Sure.'
    elif hey_bob.isupper():
        return 'Whoa, chill out!' 
    else:
        return 'Whatever.'
 
print(response(hey_bob))
