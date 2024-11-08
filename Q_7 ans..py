# Write a code to convert a given string to uppercase or lowercase

def convert_case(s, to_upper=True):
    if to_upper:
        return s.upper()  # Convert to uppercase
    else:
        return s.lower()  # Convert to lowercase

# Test the function
string = "Hello, World!"

# Convert to uppercase
upper_string = convert_case(string, to_upper=True)
print("Uppercase:", upper_string)

# Convert to lowercase
lower_string = convert_case(string, to_upper=False)
print("Lowercase:", lower_string)

