#  Write a code to merge two sorted lists into a single sorted list


def merge_sorted_lists(list1, list2):
    i, j = 0, 0  # Pointers for both lists
    merged_list = []  # Result list to store merged elements
    
    # Loop through both lists until one is exhausted
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    # Append any remaining elements from list1
    merged_list.extend(list1[i:])
    
    # Append any remaining elements from list2
    merged_list.extend(list2[j:])
    
    return merged_list

# Example usage
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
result = merge_sorted_lists(list1, list2)
print(result)

