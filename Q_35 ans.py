# Write a code that inverts a dictionary, swapping keys and values. Ensure that the inverted dictionary correctly handles cases where multiple keys have the same value by storing the keys as a list in the inverted dictionary

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
