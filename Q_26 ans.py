# Write a code that prompts the user to input two sets of characters. Then, print the union of these two sets 

def main():
    # Prompt the user to enter two sets of characters
    set1_input = input("Enter the first set of characters, separated by commas: ")
    set2_input = input("Enter the second set of characters, separated by commas: ")
    
    # Convert the input strings into sets of characters
    set1 = set(set1_input.split(','))
    set2 = set(set2_input.split(','))
    
    # Find the union of the two sets
    union = set1 | set2
    
    # Print the result
    print("The union of the two sets is:", union)

# Call the main function
main()
