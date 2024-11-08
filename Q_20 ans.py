# Write a code to shuffle a given list randomly without using any built-in shuffle functions



import random

def shuffle_list(lst):
    # Iterate through the list from the last element to the second element
    for i in range(len(lst) - 1, 0, -1):
        # Pick a random index from 0 to i
        j = random.randint(0, i)
        
        # Swap the elements at index i and index j
        lst[i], lst[j] = lst[j], lst[i]
    
    return lst

# Example usage
lst = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(lst)
print(shuffled_list)

