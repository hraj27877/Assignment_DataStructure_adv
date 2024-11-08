#  Develop a code that takes a tuple of integers as input. The function should return the maximum and minimum values from the tuple using tuple unpacking


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
