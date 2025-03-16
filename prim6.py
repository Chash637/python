# Function to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Function to check if a number is prime
def check_prime(num):
    if num <= 1:
        return "Not Prime"
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return "Not Prime"
    return "Prime"

# Main function to drive the menu
def main():
    while True:
        print("\nMenu:")
        print("1. Check if a number is even or odd")
        print("2. Check if a number is prime")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            num = int(input("Enter a number: "))
            result = check_even_odd(num)
            print(f"The number {num} is {result}.")
        
        elif choice == '2':
            num = int(input("Enter a number: "))
            result = check_prime(num)
            print(f"The number {num} is {result}.")
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Calling the main function
if __name__ == "__main__":
    main()
