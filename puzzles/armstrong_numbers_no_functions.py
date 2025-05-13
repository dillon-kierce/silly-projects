"""
This is an armstrong number verifier
"""

input = int(input("Enter a valid number: "))
length = len(str(input))
numbers = [int(x) for x in str(input)]
sum_numbers = sum(numbers)
raised = [x ** int(length) for x in numbers]
sum_numbers = sum(raised)
if sum_numbers == input:
    print("You have found a armstrong number! ")
else:
    print("Invalid number try again")
