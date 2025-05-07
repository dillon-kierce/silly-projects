"""
This is the collatz conjecture which has a rule to always get to the value of one
If the value is even then divide by 2 until unable to do so
If odd multiply by 3 and add 1
Negotiating between these two will allow you to theoretically always get to one
"""


number = int(input('Please enter a valid integer for this to work: '))

def steps(number):
    """
    Utilized to basically say if the number is even do this, and if its odd do that
    Until it reaches 1 this does all the mathmatical calculation but doesnt count steps
    """
    step_calc = 0
    while number != 1:
        if number % 2 == 0:
            number = number / 2
            print(number)
            step_calc = step_calc + 1
        elif number % 2 != 0:
                number = number * 3 + 1
                print(number)
                step_calc = step_calc + 1
        else:
            raise ValueError("Has to be a valid integer and not zero")
    print("This took: ", step_calc , "steps")

if number == 0 or number < 0 :
    print("Error Please retry ")
else:
    steps(number)
