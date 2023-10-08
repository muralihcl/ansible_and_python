# Example of functions

# Generalized function which can work with any 2 numerical inputs
def operations(num1, num2):
    print(f"Sum of {num1} and {num2} is: {num1 + num2}")
    print(f"Difference of {num1} and {num2} is: {num1 - num2}")
    print(f"Product of {num1} and {num2} is: {num1 * num2}")
    print(f"Quotient of {num1} and {num2} is: {num1 / num2}")
    print(f"Integer Quotient of {num1} and {num2} is: {num1 // num2}")
    print(f"Remainder of {num1} and {num2} division is: {num1 % num2}")

# Hard coded function which is not useful when different inputs are to be given
def operations_hc():
    print(f"Sum of {number1} and {number2} is: {number1 + number2}")
    print(f"Difference of {number1} and {number2} is: {number1 - number2}")
    print(f"Product of {number1} and {number2} is: {number1 * number2}")
    print(f"Quotient of {number1} and {number2} is: {number1 / number2}")
    print(f"Integer Quotient of {number1} and {number2} is: {number1 // number2}")
    print(f"Remainder of {number1} and {number2} division is: {number1 % number2}")

def test_print():
    print("This is a sample print statement")

number1 = 25
number2 = 6

test_print()

number3 = 23
number4 = 4
# operations(number1, number2) # Calling the function using positional variables
# operations(number2, number1)
# operations(num2=number2, num1=number1) # Calling the function using direct assignment of variables

# Calling operations_hc (hardcoded function) works only against number1 and number2
operations_hc()

# Generalized operation can work with any number if we just align it to the function level variables it is accepting
operations(num1=number1, num2=number2)
operations(num1=number3, num2=number4)
operations(number1, number4)
