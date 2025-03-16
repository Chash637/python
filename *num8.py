def pattern_1():
    # This pattern starts with 4 stars and reduces the count by 1 each line.
    for i in range(4, 0, -1):
        print('* ' * i)

def pattern_2():
    # This pattern starts with 1 star and increases the count by 1 each line.
    for i in range(1, 5):
        print('* ' * i)

def main():
    while True:
        # Display the menu
        print("\nMenu:")
        print("1. Display Pattern i")
        print("2. Display Pattern ii")
        print("3. Exit")
        
        # Get user choice
        choice = int(input("Enter your choice (1/2/3): "))
        
        if choice == 1:
            print("\nPattern i:")
            pattern_1()  # Display Pattern i
        elif choice == 2:
            print("\nPattern ii:")
            pattern_2()  # Display Pattern ii
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please enter a valid option.")

if __name__ == "__main__":
    main()
