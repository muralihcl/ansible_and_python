# Print the message Hello Python using print function
# print("Hello Python")

# Assign a value to the variable myname (string)
my_name = "Muralidhara Kakkunje"
# Print the variable value without any formatting
print(my_name)

# Print formatted message with .format method
print("Hello, my name is {}".format(my_name))

# Print formatted message with f string method
print(f"Hello, my name is {my_name}")

# Assign a value to the variable my age (int)
my_age = 42

# Printing further message with format method and automatic sequencing
print("Hello, my name is {} and I am {} years old".format(my_name, my_age))

# Printing further message with format method and indexed sequencing
print("Hello, my name is {0} and I am {1} years old".format(my_name, my_age))

# Printing further message with format method and indexed sequencing with variables interchanged
print("Hello, my name is {1} and I am {0} years old".format(my_name, my_age))

# Printing further message with f string method double-quoted
print(f"Hello, my name is {my_name} and I am {my_age} years old")

# Printing further message with f string method single-quoted
print(f'Hello, my name is {my_name} and I am {my_age} years old')

# Print the data type of the variable my_name and my_age using f string method (introduction of new line character \n)
print(f"The datatype of variable myname is {type(my_name)} \nThe datatype of variable my_age is {type(my_age)}")

# Not allowed variable names
# 1 = my_name # Variable name cannot be a literal or integer
# 1myname = my_name # Variable name cannot start with a number
# int = my_name # Cannot be a keyword
# my-name = my_name1 # Variable name cannot include - as it is a valid operator within python

# Assigning a new variable with another variable => This is copy (but not deep copy)
my_name1 = my_name
my_name2 = "Muralidhara Kakkunje"

# Print message with values of my_name and my_name1 variables along with memory locations (notice both of them carry same memory location
# This is how python efficiently manages memory (same values are allocated same memory location)
print(f"The value of variable my_name is {my_name}, value of variable my_name1 is {my_name1} and value of variable my_name2 is {my_name2}")
print(f"ID of variable my_name is {id(my_name)}, ID of variable my_name1 is {id(my_name1)} and ID of variable my_name2 is {id(my_name2)}")

# The moment variable gets reassigned, it will get a new memory location
my_name = "Devinder Singh"
print(f"The value of variable my_name is {my_name}, value of variable my_name1 is {my_name1} and value of variable my_name2 is {my_name2}")
print(f"ID of variable my_name is {id(my_name)}, ID of variable my_name1 is {id(my_name1)} and ID of variable my_name2 is {id(my_name2)}")

"""
This is a multi-line comment
spanning across multiple lines
"""

'''
This is also a valie method to include multi-line comment
spanning across multiple lines
'''

# Text wrapping example with \
my_bigger_variable_name_one = "The "
my_bigger_variable_name_two = "quick "
my_bigger_variable_name_three = "brown "
my_bigger_variable_name_four = "fox "
my_bigger_variable_name_five = "jumps "
my_bigger_variable_name_six = "over "
my_bigger_variable_name_seven = "the "
my_bigger_variable_name_eight = "lazy "
my_bigger_variable_name_nine = "dog "

my_big_combined_variable = my_bigger_variable_name_one + my_bigger_variable_name_two + my_bigger_variable_name_three + my_bigger_variable_name_four + \
    my_bigger_variable_name_five + my_bigger_variable_name_six + my_bigger_variable_name_seven + my_bigger_variable_name_eight + \
    my_bigger_variable_name_nine
print(my_big_combined_variable)

# Combined variable assignment in
my_name, my_age, my_weight = 'Muralidhara Kakkunje', 42, 84.5
print(my_name, my_age, my_weight)

# Swap variable values
learner1, learner2 = 'Devinder Singh', 'Swaminathan C'
print(learner1, learner2)
learner1, learner2 = learner2, learner1
print(learner1, learner2)

# Chained variable assignment
var1 = var2 = var3 = var4 = None
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
