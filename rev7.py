def reverse_number(num):
    # Reverse the number without converting it to a string
    reversed_num = 0
    original_num = num
    
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    
    # Check if the number is a palindrome
    if original_num == reversed_num:
        print(f"The number {original_num} is a palindrome.")
    else:
        print(f"The number {original_num} is not a palindrome.")
    
    return reversed_num

def reverse_string(s):
    # Reverse the string
    return s[::-1]

def main():
    choice = input("Do you want to reverse a number or a string? (Enter 'number' or 'string'): ").lower()
    
    if choice == 'number':
        num = int(input("Enter the number you want to reverse: "))
        reversed_num = reverse_number(num)
        print(f"The reversed number is: {reversed_num}")
    
    elif choice == 'string':
        s = input("Enter the string you want to reverse: ")
        reversed_str = reverse_string(s)
        print(f"The reversed string is: {reversed_str}")
    
    else:
        print("Invalid choice. Please enter 'number' or 'string'.")

if __name__ == "__main__":
    main()
