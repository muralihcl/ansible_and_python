# Simple data types: Integer, String, Float, Long

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

# Print a portion of the list
print("Print a portion of the list")
print(my_list[:2])
print(my_list[0:])

my_big_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_big_list[::-1])
print(my_big_list[0:7:2])
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

# Strings a sequence types
string = "Hello, world!"

# Slicing
print("Printing Slices")
# Syntax for slicing is start:end => Anything omitted will be defaulted start=0, end=n
print(string[:5])
print(string[-6:-1])
print(string[-9:])
print(string[:-8])
print(string[:])

# Substring
print("Printing Substrings")
# Syntax for substring is start:end:step => Anything omitted will be defaulted start=0, end=n, step=1
print(string[3:9:2]) #returns the substring s[3]s[5]s[7] => 'l,w'
print(string[3:6:3]) #returns the substring s[3] => 'l'
print(string[:5:2]) #returns the substring s[0]s[2]s[4] => 'Hlo'
print(string[::-1]) #returns the reverted string => '!dlrow ,olleH'
print(string[::-2]) #returns the substring s[-1]s[-3]s[-5]s[-7]s[-9]s[-11]s[-13] => '!lo olH'

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

print("List operations")
# List operations pop, del, clear, sort, copy, count, append, extend, index, insert, remove, reverse etc
# pop => pops out last element from the list, it also returns the popped item
# del => delete a specific item from the list, it doesn't return anything
# clear => Clears all the contents of the list, in-place, it doesn't return anything
# sort => sorts numerically/alphabetically according to ASCII table, doesn't return anything
# append => Takes a single value and appends after the last element in the list
# extend => Takes another list and appends the elements of the new list after the last element of the existing list

my_popped_item = my_example_list.pop()
print(my_example_list)
print(my_popped_item)

my_example_list[2] = 'Pineapple'
print(my_example_list)

del(my_example_list[1])
print(my_example_list)

# Sort with numerical values
my_dup_list.sort()
print(my_dup_list)

my_text_list = ['Murali', 'Devinder', 'Unni', 'Swami', 'unni', 'murali', 'swamy', 'devinder']
print(my_text_list.sort()) # Print returns None as sort does not return anything
print(my_text_list)

my_list_of_cleared_items = my_example_list.clear()
print(my_example_list)
print(my_list_of_cleared_items)

my_example_list.append('Murali')
my_example_list.append('Swaminathan')
my_example_list.append('Devinder')
print(my_example_list)

# Extend merges the items of my_text_list into my_example_list
my_example_list.extend(my_text_list)
print(my_example_list)

# Append of the same my_test_list results in my_text_list getting appended as a list at the end of the current my_example_list
my_example_list.append(my_text_list)
print(my_example_list)

# Complex operations are permitted as far as we know what we are doing. In the below example, individual operations are treating previous operations output as input
print(my_example_list[-1][0:3][0])

# Dictionaries => Dictionaries are enclosed within curly braces and individual items are key-value pairs. So, dictionaries do not have index way of reference
# Individual items are referred by their keys
my_dict = {'name': "Murali", 'age': 42, 'weight': 84.5, 'skills': ['Linux', 'DevOps', 'Automation']}
print(my_dict)
print(my_dict['name'])
print(my_dict['age'])
print(my_dict['weight'])
print(my_dict['skills'])

# Initialize a new empty dictionary (this is not going to be treated as empty set by Python, but treated as empty dictionary)
my_new_dict = {}
print(type(my_new_dict))
# We can keep assigning key and values like this
my_new_dict['name'] = 'Devinder Singh'
my_new_dict['age'] = 47
my_new_dict['weight'] = 84.5
my_new_dict['skills'] = ['Linux', 'Automation', 'Clustering']
print(my_new_dict)

# Using set to remove duplicates
print("Using set to remove duplictes from lists and tuples")
my_list_with_duplicates = ['banana', 'apple', 'apple', 'orange', 'orange']
my_list_without_duplicates = list(set(my_list_with_duplicates))
print(my_list_without_duplicates)

my_tuple_with_duplicates = ('banana', 'apple', 'apple', 'orange', 'orange')
my_tuple_without_duplicates = tuple(set(my_tuple_with_duplicates))
print(my_tuple_without_duplicates)

