def compute_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def print_fibonacci_series(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i - 1] + fib_series[i - 2])
    return fib_series

def main():
    print("Choose an option:")
    print("1. Compute Factorial")
    print("2. Print Fibonacci Series")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        number = int(input("Enter a number to compute the factorial: "))
        print(f"The factorial of {number} is {compute_factorial(number)}")
    elif choice == '2':
        terms = int(input("Enter the number of terms in the Fibonacci series: "))
        print(f"The Fibonacci series up to {terms} terms is: {print_fibonacci_series(terms)}")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
