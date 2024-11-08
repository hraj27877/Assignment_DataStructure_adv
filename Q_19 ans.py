#  Create a code to find the union of two lists without duplicates


def union_of_lists(list1, list2):
    # Convert both lists to sets and find the union
    set1 = set(list1)
    set2 = set(list2)
    
    # Use the | operator to find the union of both sets
    union = list(set1 | set2)
    
    return union

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
result = union_of_lists(list1, list2)
print(result)

