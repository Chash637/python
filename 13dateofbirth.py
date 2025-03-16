import re

# Function to validate email address
def validate_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern, email):
        return "Valid Email"
    else:
        return "Invalid Email"

# Function to validate date in DD/MM/YYYY or MM-DD-YYYY format
def validate_date(date):
    date_pattern = r'^(0[1-9]|[12][0-9]|3[01])[-/](0[1-9]|1[0-2])[-/]\d{4}$'
    if re.match(date_pattern, date):
        return "Valid Date"
    else:
        return "Invalid Date"

# Main program
def main():
    # Input email validation
    email = input("Enter an email address: ")
    print(validate_email(email))
    
    # Input date validation
    date = input("Enter a date (DD/MM/YYYY :")
    print(validate_date(date))

# Run the program
if __name__ == "__main__":
    main()
