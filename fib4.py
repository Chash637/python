# Recursive function to print Fibonacci series up to n_terms
def fibonacci(n_terms, a=0, b=1):
    # Base case: when n_terms is 0 or negative, stop the recursion
    if n_terms <= 0:
        return
    else:
        # Print the current term (a)
        print(a, end=" ")
        # Recursive call: Decrease n_terms and shift the values for next terms
        fibonacci(n_terms - 1, b, a + b)

# Main program
n_terms = int(input("Enter the number of terms in the Fibonacci series: "))
print("Fibonacci Series:")
fibonacci(n_terms)
