# Operations in python
# Operations on numerical datatypes
# + => Addition, - is subtraction, * is multiplication, / is division, // is integer division, % is mod/remainder
# + & * are available even for strings
# Sequence datatypes like lists and tuples also support similar operations

# Integer operations
num1 = 5
num2 = 2
print(f"Sum of {num1} and {num2} is: {num1+num2}")
print(f"Difference of {num1} and {num2} is: {num1-num2}")
print(f"Product of {num1} and {num2} is: {num1*num2}")
print(f"Quotient of {num1} and {num2} is: {num1/num2}")
print(f"Integer Quotient of {num1} and {num2} is: {num1//num2}")
print(f"Remainder of {num1} and {num2} division is: {num1%num2}")

# String operations
string1 = '*'
string2 = "good"
print(30*string1)
print("A generic heading")
print(30*string1)
# print(string1*string2) => not right
print(5*string2)
print(string1 + string2) # + is used for string concatenation
print("The concatenation of string1 and string2 is " + string1+string2 + str(5)) # To concatenate an integer, we need to convert it to string as string cannot operate with any other datatypes

# Operations on lists
my_list = [1, 2, 3, 4]
my_small_list = [1, 2]
print(my_list)
print(5 * my_list)
print(my_list + my_list)
# print(my_list - my_small_list) => operation - is not defined for list

# Operations on tuples
my_tup = (1, 2, 3, 4)
my_small_tup = (1, 2)
print(my_tup)
print(5 * my_tup)
print(my_tup + my_small_tup)

# Operations on dictionaries
my_dict = {'name': 'Murali', 'age': 42, 'weight': 84.5}
my_dict2 = {'name': 'Devinder', 'age': 47, 'weight': 84.5}
my_dict.update(my_dict2)
print(my_dict)

