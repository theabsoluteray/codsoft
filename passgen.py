# Importing libraries

import string
import random


# function which generates the password based on input
def gen_pass(length, complexity):
    
    # checking if the length is valid
    if length <= 0:
        return "Password length must be greater than 0."

    # Define character pools
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation

    if complexity == 1:
        char_combinations = letters
    elif complexity == 2:
        char_combinations = letters + digits
    elif complexity == 3:
        char_combinations = letters + digits + special_characters
    else:
        return "Invalid complexity level. Choose 1, 2, or 3."

    # Generate password
    password = ''.join(random.choice(char_combinations) for _ in range(length))
    return password

# User input
try:

    # taking input for password length
    length = int(input("Enter the desired password length: "))

    # taking input for comlexity level
    complexity = int(input("Enter the complexity level (1-Letters, 2-Letters & Digits, 3-Letters, Digits & Special Characters): "))
    password = gen_pass(length, complexity)
    print(f"Generated Password: {password}")

#handling wrong input
except ValueError:
    print("Please enter valid numbers for length and complexity.")
