#  Implement a code to find and remove duplicates from a list while preserving the original order of elements


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
