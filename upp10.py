# Function to calculate counts of uppercase, lowercase, digits, and special characters
def calculate_character_counts(s):
    upper_count = 0
    lower_count = 0
    digit_count = 0
    special_count = 0

    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_count += 1  # For any other character (special characters)

    return upper_count, lower_count, digit_count, special_count

# Main program
input_string = input("Enter a string: ")
upper, lower, digits, special = calculate_character_counts(input_string)

# Display the results
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
print(f"Digits: {digits}")
print(f"Special characters: {special}")
