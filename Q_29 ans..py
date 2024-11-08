# Write a code that takes a tuple and an element as input. The function should return the count of occurrences of the given element in the tuple

def count_occurrences(input_tuple, element):
    # Return the count of occurrences of the element in the tuple
    return input_tuple.count(element)

# Example usage
tuple_input = tuple(map(int, input("Enter a tuple of integers, separated by commas: ").split(',')))
element = int(input("Enter the element to count: "))

count = count_occurrences(tuple_input, element)
print(f"The element {element} appears {count} time(s) in the tuple.")
