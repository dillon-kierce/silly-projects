"""
This is an armstrong number verifier
"""
input = int(input("Enter a valid number: "))

def is_armstrong_number(input):
    """
    Takes a value, splits into a list, and takes the power of length across all digits to dictate if its armstrong number
    """
    length = len(str(input))
    numbers = [int(x) for x in str(input)]
    sum_raised = sum([x ** int(length) for x in numbers])
    if sum_raised == input:
        print("You have found a armstrong number! ")
    else:
        print("Invalid number try again")

is_armstrong_number(input)
