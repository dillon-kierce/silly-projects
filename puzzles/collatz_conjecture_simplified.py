"""
This is the collatz conjecture which has a rule to always get to one
If the value is even then divide by 2 until unable to do so
If odd multiply by 3 and add 1
Negotiating between these two will allow you to theoretically always get to one
"""


number = int(input('Please enter a valid integer for this to work: '))

def steps(number):
    if number < 1:
        raise ValueError("Only valid postive integers are allowed")
    counter = 0
    """
    Utilized to basically say if the number is even do this, and if its odd do that
    Until it reaches 1 this does all the mathmatical calculation but doesnt count steps
    """
    while number > 1:
        number = 3 * number + 1 if number % 2 else number / 2
        counter += 1
    return counter
print(steps(number))
