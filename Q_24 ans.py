# Develop a code that prompts the user to input two sets of strings. Then, print the elements that are present in the first set but not in the second set


def main():
    # Prompt the user to enter two sets of strings
    set1_input = input("Enter the first set of strings, separated by commas: ")
    set2_input = input("Enter the second set of strings, separated by commas: ")
    
    # Convert the input strings into sets of strings
    set1 = set(set1_input.split(','))
    set2 = set(set2_input.split(','))
    
    # Find the elements present in set1 but not in set2
    difference = set1 - set2
    
    # Print the result
    print("The elements present in the first set but not in the second set:", difference)

# Call the main function
main()
