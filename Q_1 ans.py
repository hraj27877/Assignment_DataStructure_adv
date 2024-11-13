# <1> REVERSEING A STRING

a= "hello world"
b=a[::-1]
print(b)


# <2> Program to count the no. of vovels in a string

a = "hello world"
c=0
for i in a:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        c=c+1
print (c)


# <3> Write a code to check if a given string is a palindrome or not.

def is_palindrome(string):
    # Convert the string to lowercase and remove spaces
    cleaned_string = string.replace(" ", "").lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Test the function
string = "A man a plan a canal Panama"
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    
    
    
# <4> Write a code to check if two given strings are anagrams of each other

def are_anagrams(string1, string2):
    # Remove spaces, convert to lowercase, and sort both strings
    cleaned_string1 = ''.join(sorted(string1.replace(" ", "").lower()))
    cleaned_string2 = ''.join(sorted(string2.replace(" ", "").lower()))
    
    # Check if the sorted versions of both strings are the same
    return cleaned_string1 == cleaned_string2

# Test the function
string1 = "listen"
string2 = "silent"
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
    
    
    
# <5> Write a code to find all occurrences of a given substring within another string

def find_occurrences(main_string, substring):
    occurrences = []
    start = 0

    while True:
        # Find the next occurrence of the substring
        index = main_string.find(substring, start)
        
        # If no more occurrences are found, break the loop
        if index == -1:
            break
        
        # Add the index to the list of occurrences
        occurrences.append(index)
        
        # Move the start position to the next character after the found occurrence
        start = index + 1

    return occurrences

# Test the function
main_string = "This is a test string and this is just a test."
substring = "is"
positions = find_occurrences(main_string, substring)
print("Occurrences of substring found at positions:", positions)




# <6> Write a code to determine if a string has all unique characters

def has_unique_characters(s):
    # Use a set to track characters we've seen
    seen_characters = set()

    # Loop through each character in the string
    for char in s:
        # If the character is already in the set, it's not unique
        if char in seen_characters:
            return False
        # Otherwise, add the character to the set
        seen_characters.add(char)

    # If we complete the loop without finding duplicates, all characters are unique
    return True

# Test the function
string = "abcdefg"
if has_unique_characters(string):
    print("The string has all unique characters.")
else:
    print("The string does not have all unique characters.")
    
    
    
    
# <7> Write a code to convert a given string to uppercase or lowercase

def convert_case(s, to_upper=True):
    if to_upper:
        return s.upper()  # Convert to uppercase
    else:
        return s.lower()  # Convert to lowercase

# Test the function
string = "Hello, World!"

# Convert to uppercase
upper_string = convert_case(string, to_upper=True)
print("Uppercase:", upper_string)

# Convert to lowercase
lower_string = convert_case(string, to_upper=False)
print("Lowercase:", lower_string)



# <8> Write a code to convert a given string to uppercase or lowercase

def convert_case(s, to_upper=True):
    if to_upper:
        return s.upper()  # Convert to uppercase
    else:
        return s.lower()  # Convert to lowercase

# Test the function
string = "Hello, World!"

# Convert to uppercase
upper_string = convert_case(string, to_upper=True)
print("Uppercase:", upper_string)

# Convert to lowercase
lower_string = convert_case(string, to_upper=False)
print("Lowercase:", lower_string)



# <9> Write a code to count the number of words in a string


def count_words(string):
    words = string.split()  # Split the string by whitespace
    return len(words)  # Return the number of words


text = "Hello, how many words are in this sentence?"
print("Number of words:", count_words(text))



# <10> Write a code to concatenate two strings without using the + operator.

string1 = "Hello"
string2 = "World"

# Using join to concatenate
result = ''.join([string1, string2])

print(result)


# <11> Write a code to remove all occurrences of a specific element from a list..


# Original list
my_list = [1, 2, 3, 4, 2, 5, 2]

# Element to remove
element_to_remove = 2

# Using list comprehension to remove all occurrences
new_list = [item for item in my_list if item != element_to_remove]

print(new_list)


# <12> Implement a code to find the second largest number in a given list of integers

def find_second_largest(nums):
    if len(nums) < 2:
        return None  # Return None if there are fewer than 2 elements
    
    first, second = float('-inf'), float('-inf')  # Initialize variables to hold the largest and second largest numbers

    for num in nums:
        if num > first:
            second = first  # Update second largest
            first = num  # Update largest
        elif num > second and num != first:
            second = num  # Update second largest if it's smaller than first but larger than second
    
    return second if second != float('-inf') else None  # If no second largest, return None

# Example usage
nums = [12, 35, 1, 10, 34, 1]
result = find_second_largest(nums)
print(f"The second largest number is: {result}")


# <13> Create a code to count the occurrences of each element in a list and return a dictionary with elements as keys and their counts as valuekeys and their counts as value

def count_occurrences(lst):
    count_dict = {}
    for element in lst:
        if element in count_dict:
            count_dict[element] += 1  # Increment count if element exists in dictionary
        else:
            count_dict[element] = 1  # Initialize count for the element
    return count_dict

# Example usage
lst = [1, 2, 2, 3, 3, 3, 4, 5, 5]
result = count_occurrences(lst)
print(result)


# <14> Write a code to reverse a list in-place without using any built-in reverse functions


def reverse_list_in_place(lst):
    left, right = 0, len(lst) - 1  # Initialize pointers to the start and end of the list
    while left < right:
        # Swap elements at left and right
        lst[left], lst[right] = lst[right], lst[left]
        left += 1  # Move the left pointer to the right
        right -= 1  # Move the right pointer to the left
    return lst

# Example usage
lst = [1, 2, 3, 4, 5]
result = reverse_list_in_place(lst)
print(result)


#  <15> Implement a code to find and remove duplicates from a list while preserving the original order of elements


def remove_duplicates(lst):
    seen = set()  # Set to keep track of elements we've seen
    result = []  # List to store the unique elements in order
    
    for element in lst:
        if element not in seen:
            result.append(element)  # Add element to result if it is not a duplicate
            seen.add(element)  # Mark this element as seen
    
    return result

# Example usage
lst = [1, 2, 2, 3, 4, 3, 5, 5, 6]
result = remove_duplicates(lst)
print(result)


# <16> Create a code to check if a given list is sorted (either in ascending or descending order) or not


def is_sorted(lst):
    # Check if list is sorted in ascending order
    ascending = all(lst[i] <= lst[i+1] for i in range(len(lst) - 1))
    
    # Check if list is sorted in descending order
    descending = all(lst[i] >= lst[i+1] for i in range(len(lst) - 1))
    
    # Return True if the list is sorted in either order, False otherwise
    return ascending or descending

# Example usage
lst = [1, 2, 3, 4, 5]
result = is_sorted(lst)
print(f"Is the list sorted? {result}")

lst2 = [5, 4, 3, 2, 1]
result2 = is_sorted(lst2)
print(f"Is the list sorted? {result2}")

lst3 = [1, 3, 2, 4]
result3 = is_sorted(lst3)
print(f"Is the list sorted? {result3}")


# <17> Write a code to concatenate two tuples. The function should take two tuples as input and return a new tuple containing elements from both input tuples


def concatenate_tuples(tuple1, tuple2):
    # Concatenate the two tuples
    result = tuple1 + tuple2
    return result

# Example usage
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = concatenate_tuples(tuple1, tuple2)
print(result)


# <18> Implement a code to find the intersection of two given lists

def intersection_of_lists(list1, list2):
    # Convert both lists to sets and find the intersection
    set1 = set(list1)
    set2 = set(list2)
    
    # Use the & operator to find the intersection of both sets
    intersection = list(set1 & set2)
    
    return intersection

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
result = intersection_of_lists(list1, list2)
print(result)


# <19> Create a code to find the union of two lists without duplicates


def union_of_lists(list1, list2):
    # Convert both lists to sets and find the union
    set1 = set(list1)
    set2 = set(list2)
    
    # Use the | operator to find the union of both sets
    union = list(set1 | set2)
    
    return union

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
result = union_of_lists(list1, list2)
print(result)


# <20> Write a code to shuffle a given list randomly without using any built-in shuffle functions



import random

def shuffle_list(lst):
    # Iterate through the list from the last element to the second element
    for i in range(len(lst) - 1, 0, -1):
        # Pick a random index from 0 to i
        j = random.randint(0, i)
        
        # Swap the elements at index i and index j
        lst[i], lst[j] = lst[j], lst[i]
    
    return lst

# Example usage
lst = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(lst)
print(shuffled_list)



# <21> Write a code that takes two tuples as input and returns a new tuple containing elements that are common to both input tuples


def common_elements(tuple1, tuple2):
    # Convert tuples to sets and find the intersection
    set1 = set(tuple1)
    set2 = set(tuple2)
    
    # Find the intersection and convert it back to a tuple
    common = tuple(set1 & set2)
    
    return common

# Example usage
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7)
result = common_elements(tuple1, tuple2)
print(result)



# <22> Create a code that prompts the user to enter two sets of integers separated by commas. Then, print the intersection of these two sets


def main():
    # Prompt the user to enter two sets of integers
    set1_input = input("Enter the first set of integers, separated by commas: ")
    set2_input = input("Enter the second set of integers, separated by commas: ")
    
    # Convert the input strings into sets of integers
    set1 = set(map(int, set1_input.split(',')))
    set2 = set(map(int, set2_input.split(',')))
    
    # Find the intersection of the two sets
    intersection = set1 & set2
    
    # Print the intersection
    print("The intersection of the two sets is:", intersection)

# Call the main function
main()



# <23> Develop a code that prompts the user to input two sets of strings. Then, print the elements that are present in the first set but not in the second set


def main():
    # Prompt the user to enter two sets of strings
    set1_input = input("Enter the first set of strings, separated by commas: ")
    set2_input = input("Enter the second set of strings, separated by commas: ")
    
    # Convert the input strings into sets of strings
    set1 = set(set1_input.split(','))
    set2 = set(set2_input.split(','))
    
    # Find the elements present in set1 but not in set2
    difference = set1 - set2
    
    # Print the result
    print("The elements present in the first set but not in the second set:", difference)

# Call the main function
main()


# <24> Create a code that takes a tuple and two integers as input. The function should return a new tuple containing elements from the original tuple within the specified range of indices

def extract_elements_within_range(input_tuple, start_index, end_index):
    # Extract the elements within the specified range using slicing
    return input_tuple[start_index:end_index]

# Example usage
tuple_input = (10, 20, 30, 40, 50, 60, 70, 80, 90)
start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index: "))

result = extract_elements_within_range(tuple_input, start_index, end_index)
print("The elements within the specified range are:", result)


# <25> Write a code that prompts the user to input two sets of characters. Then, print the union of these two sets 

def main():
    # Prompt the user to enter two sets of characters
    set1_input = input("Enter the first set of characters, separated by commas: ")
    set2_input = input("Enter the second set of characters, separated by commas: ")
    
    # Convert the input strings into sets of characters
    set1 = set(set1_input.split(','))
    set2 = set(set2_input.split(','))
    
    # Find the union of the two sets
    union = set1 | set2
    
    # Print the result
    print("The union of the two sets is:", union)

# Call the main function
main()


#  <26> Develop a code that takes a tuple of integers as input. The function should return the maximum and minimum values from the tuple using tuple unpacking


def find_max_min(input_tuple):
    # Find the maximum and minimum values in the tuple
    max_val = max(input_tuple)
    min_val = min(input_tuple)
    
    # Return the maximum and minimum values using tuple unpacking
    return (max_val, min_val)

# Example usage
tuple_input = tuple(map(int, input("Enter a tuple of integers, separated by commas: ").split(',')))

max_val, min_val = find_max_min(tuple_input)
print(f"The maximum value is: {max_val}")
print(f"The minimum value is: {min_val}")


# <27> Create a code that defines two sets of integers. Then, print the union, intersection, and difference of these two sets


def main():
    # Define two sets of integers
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    # Calculate the union of the two sets
    union = set1 | set2
    # Calculate the intersection of the two sets
    intersection = set1 & set2
    # Calculate the difference of set1 and set2 (elements in set1 but not in set2)
    difference = set1 - set2
    
    # Print the results
    print("Union of the two sets:", union)
    print("Intersection of the two sets:", intersection)
    print("Difference of set1 and set2:", difference)

# Call the main function
main()



# <28> Write a code that takes a tuple and an element as input. The function should return the count of occurrences of the given element in the tuple

def count_occurrences(input_tuple, element):
    # Return the count of occurrences of the element in the tuple
    return input_tuple.count(element)

# Example usage
tuple_input = tuple(map(int, input("Enter a tuple of integers, separated by commas: ").split(',')))
element = int(input("Enter the element to count: "))

count = count_occurrences(tuple_input, element)
print(f"The element {element} appears {count} time(s) in the tuple.")



# <29> Develop a code that prompts the user to input two sets of strings. Then, print the symmetric difference of these two sets


def main():
    # Prompt the user to enter two sets of strings
    set1_input = input("Enter the first set of strings, separated by commas: ")
    set2_input = input("Enter the second set of strings, separated by commas: ")
    
    # Convert the input strings into sets of strings
    set1 = set(set1_input.split(','))
    set2 = set(set2_input.split(','))
    
    # Calculate the symmetric difference of the two sets
    symmetric_difference = set1 ^ set2
    
    # Print the result
    print("The symmetric difference of the two sets is:", symmetric_difference)

# Call the main function
main()



# <30> Write a code that takes a list of words as input and returns a dictionary where the keys are unique words and the values are the frequencies of those words in the input list


def word_frequencies(word_list):
    # Create an empty dictionary to store word counts
    word_count = {}
    
    # Loop through the list and count the occurrences of each word
    for word in word_list:
        if word in word_count:
            word_count[word] += 1  # Increment the count if the word is already in the dictionary
        else:
            word_count[word] = 1  # Initialize the count to 1 if it's the first occurrence
    
    return word_count

# Example usage
words_input = input("Enter a list of words, separated by spaces: ").split()

# Get the word frequencies
result = word_frequencies(words_input)

# Print the resulting dictionary
print("Word frequencies:", result)



# <31> Write a code that takes a list of words as input and returns a dictionary where the keys are unique words and the values are the frequencies of those words in the input list


def word_frequencies(word_list):
    # Create an empty dictionary to store word counts
    word_count = {}
    
    # Loop through the list and count the occurrences of each word
    for word in word_list:
        if word in word_count:
            word_count[word] += 1  # Increment the count if the word is already in the dictionary
        else:
            word_count[word] = 1  # Initialize the count to 1 if it's the first occurrence
    
    return word_count

# Example usage
words_input = input("Enter a list of words, separated by spaces: ").split()

# Get the word frequencies
result = word_frequencies(words_input)

# Print the resulting dictionary
print("Word frequencies:", result)



# <32> Write a code to access a value in a nested dictionary. The function should take the dictionary and a list of keys as input, and return the corresponding value. If any of the keys do not exist in the dictionary, the function should return None


def access_nested_dict_value(nested_dict, keys):
    # Loop through each key in the list
    for key in keys:
        # Check if the key exists in the current dictionary level
        if key in nested_dict:
            # Move to the next level of the dictionary (or the final value if it's a leaf)
            nested_dict = nested_dict[key]
        else:
            # Return None if any key is not found
            return None
    # Return the final value if all keys are found
    return nested_dict

# Example usage
nested_dict = {
    "a": {
        "b": {
            "c": 10,
            "d": 20
        },
        "e": 30
    },
    "f": 40
}

# List of keys to access
keys = ["a", "b", "c"]

# Access the value using the function
result = access_nested_dict_value(nested_dict, keys)
print("The value is:", result)



# <33> Write a code that takes a dictionary as input and returns a sorted version of it based on the values. You can choose whether to sort in ascending or descending order


def sort_dict_by_value(input_dict, descending=False):
    # Sort the dictionary by its values
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=descending))
    return sorted_dict

# Example usage
input_dict = {"apple": 5, "banana": 2, "orange": 8, "grape": 1}

# Ask the user for the sort order
order = input("Enter 'asc' for ascending or 'desc' for descending: ").strip().lower()

# Sort the dictionary based on the user's input
descending = True if order == 'desc' else False

sorted_result = sort_dict_by_value(input_dict, descending)

print("Sorted Dictionary:", sorted_result)



# <34> Write a code that inverts a dictionary, swapping keys and values. Ensure that the inverted dictionary correctly handles cases where multiple keys have the same value by storing the keys as a list in the inverted dictionary

def invert_dict(input_dict):
    inverted_dict = {}

    # Loop through the original dictionary
    for key, value in input_dict.items():
        # If the value is not already a key in the inverted dictionary, initialize it as a list
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        else:
            # If the value is already in the inverted dictionary, append the key to the list
            inverted_dict[value].append(key)

    return inverted_dict

# Example usage
input_dict = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}

inverted_result = invert_dict(input_dict)

print("Inverted Dictionary:", inverted_result)











