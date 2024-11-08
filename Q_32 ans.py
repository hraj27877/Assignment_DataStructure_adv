# Write a code that takes two dictionaries as input and merges them into a single dictionary. If there are common keys, the values should be added together


def merge_dicts(dict1, dict2):
    # Create a new dictionary to store the merged result
    merged_dict = dict1.copy()  # Copy the first dictionary to start with

    # Loop through the second dictionary and merge values
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  # Add the values if the key exists in both dictionaries
        else:
            merged_dict[key] = value  # Otherwise, just add the key-value pair

    return merged_dict

# Example usage
dict1 = {"apple": 3, "banana": 2, "orange": 5}
dict2 = {"banana": 1, "grape": 4, "apple": 2}

merged_result = merge_dicts(dict1, dict2)

print("Merged Dictionary:", merged_result)
