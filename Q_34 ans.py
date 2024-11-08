#  Write a code that takes a dictionary as input and returns a sorted version of it based on the values. You can choose whether to sort in ascending or descending order


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
