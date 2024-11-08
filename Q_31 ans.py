# Write a code that takes a list of words as input and returns a dictionary where the keys are unique words and the values are the frequencies of those words in the input list


def word_frequencies(word_list):
    # Create an empty dictionary to store word counts
    word_count = {}
    
    # Loop through the list and count the occurrences of each word
    for word in word_list:
        if word in word_count:
            word_count[word] += 1  # Increment the count if the word is already in the dictionary
        else:
            word_count[word] = 1  # Initialize the count to 1 if it's the first occurrence
    
    return word_count

# Example usage
words_input = input("Enter a list of words, separated by spaces: ").split()

# Get the word frequencies
result = word_frequencies(words_input)

# Print the resulting dictionary
print("Word frequencies:", result)
