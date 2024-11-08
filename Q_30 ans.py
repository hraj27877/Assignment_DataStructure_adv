# Develop a code that prompts the user to input two sets of strings. Then, print the symmetric difference of these two sets


def main():
    # Prompt the user to enter two sets of strings
    set1_input = input("Enter the first set of strings, separated by commas: ")
    set2_input = input("Enter the second set of strings, separated by commas: ")
    
    # Convert the input strings into sets of strings
    set1 = set(set1_input.split(','))
    set2 = set(set2_input.split(','))
    
    # Calculate the symmetric difference of the two sets
    symmetric_difference = set1 ^ set2
    
    # Print the result
    print("The symmetric difference of the two sets is:", symmetric_difference)

# Call the main function
main()
