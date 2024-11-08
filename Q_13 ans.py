# Create a code to count the occurrences of each element in a list and return a dictionary with elements as keys and their counts as valuekeys and their counts as value

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
