# Implement a code to find the intersection of two given lists

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

