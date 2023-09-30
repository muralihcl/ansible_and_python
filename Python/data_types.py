# Simple data types: Integers, Strings, Floats

# String variable
my_name = "Muralidhara Kakkunje"
print(len(my_name))

# Integer variable
my_age = 42
my_age1 = "42"

# Float variable
my_weight = 84.5

# Print the data types
print(f"Data type of my_name is {type(my_name)}, data type of my_age is {type(my_age)} and data type of my_weight is {type(my_weight)}")
print(f"My name is {my_name}, I am {my_age} years old and I weigh {my_weight}kg")

# Casting
print(type(int(my_weight)))
print(type(int(my_age1)))
print(type(float(my_age)))

print(my_name, my_age, my_age1, my_weight)
print(type(my_name), type(my_age), type(my_age1), type(my_weight))

# Complex data types
# List
my_list = ["Muralidhara Kakkunje", 42, 84.5]
print(my_list)
print(type(my_list))

# Access the elements of List
print(my_list[0])
print(my_list[1])
print(my_list[2])

# print(my_list[3]) # List index out of range as list index starts from 0

# Print the length of the list (or number of items in the list)
print(len(my_list))

# Looping through list items
for item in my_list:
    print(item)

# Set (contains/retains only unique items) enclosed within curly braces
my_set_int = {3, 2, 1, 1, 3, 2}
print(my_set_int)
print(type(my_set_int))
print(len(my_set_int))
print()
for item in my_set_int:
    print(item)

# Set retains only unique values even if there is an error during initial assignments
my_set_comb = {'Muralidhara Kakkunje', 42, 84.5, 84.5}

print(my_set_comb)

# Using set to remove duplicates from a list
my_dup_list = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
# Two-step procedure to get a list with unique items
my_uniq_set = set(my_dup_list)
my_uniq_list = list(my_uniq_set)

# One-step procedure with double casting to get the list with unique items
my_uniq_list1 = list(set(my_dup_list))

print(my_dup_list)
print(my_uniq_list)
print(my_uniq_list1)

# Tuples
my_tup = ('Muralidhara Kakkunje', 42, 84.5)
print(type(my_tup))
print(len(my_tup))
print(my_tup)

# Tuple is immutable => We can only reassign the value of a tuple, but, individual elements cannot be changed
# List is mutable => We can change individual values also
my_example_list = ['Banana', 'Orange', 'Apple', 'Grapes']
my_example_tuple = ('Banana', 'Orange', 'Apple', 'Grapes')
print(my_example_list)

my_example_list.pop()
print(my_example_list)

my_example_list[2] = 'Pineapple'
print(my_example_list)
