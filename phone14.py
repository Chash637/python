import re

# Function to validate URL
def validate_url(url):
    url_pattern = r'^(https?://)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(url_pattern, url):
        return "Valid URL"
    else:
        return "Invalid URL"

# Function to validate Phone Number
def validate_phone(phone):
    phone_pattern = r'^\d{3}-?\d{3}-?\d{4}$'
    if re.match(phone_pattern, phone):
        return "Valid Phone Number"
    else:
        return "Invalid Phone Number"

# Main program
def main():
    # Input URL validation
    url = input("Enter a URL (http:// or https://): ")
    print(validate_url(url))
    
    # Input phone number validation
    phone = input("Enter a phone number (e.g., 123-456-7890 or 1234567890): ")
    print(validate_phone(phone))

# Run the program
if __name__ == "__main__":
    main()
