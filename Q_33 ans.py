#Write a code to access a value in a nested dictionary. The function should take the dictionary and a list of keys as input, and return the corresponding value. If any of the keys do not exist in the dictionary, the function should return None


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
