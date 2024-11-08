# Write a code to count the number of words in a string


def count_words(string):
    words = string.split()  # Split the string by whitespace
    return len(words)  # Return the number of words


text = "Hello, how many words are in this sentence?"
print("Number of words:", count_words(text))
