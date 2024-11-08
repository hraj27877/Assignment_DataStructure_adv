#  Write a code to remove all occurrences of a specific element from a list..


# Original list
my_list = [1, 2, 3, 4, 2, 5, 2]

# Element to remove
element_to_remove = 2

# Using list comprehension to remove all occurrences
new_list = [item for item in my_list if item != element_to_remove]

print(new_list)
