# Create a code that takes a tuple and two integers as input. The function should return a new tuple containing elements from the original tuple within the specified range of indices

def extract_elements_within_range(input_tuple, start_index, end_index):
    # Extract the elements within the specified range using slicing
    return input_tuple[start_index:end_index]

# Example usage
tuple_input = (10, 20, 30, 40, 50, 60, 70, 80, 90)
start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index: "))

result = extract_elements_within_range(tuple_input, start_index, end_index)
print("The elements within the specified range are:", result)
