# Bisection Method Implementation in Python
def f(x):
    """ Define the function f(x) = x^3 - 2x - 5 """
    return x**3 - 2*x - 5
def bisection_method(a, b, iterations):
    """
    Bisection Method to find root of f(x) = 0
    Parameters:
    a : lower bound of interval
    b : upper bound of interval
    iterations : number of iterations to perform
    """
    # Check if interval is valid
    if f(a) * f(b) >= 0:
        print("Invalid interval!")
        return None
    # Print table header
    print("Iter\ta\t\tb\t\tx_n\t\tf(x_n)")
    print("-" * 65)
    # Perform iterations
    for i in range(1, iterations + 1):
        # Calculate midpoint
        x_n = (a + b) / 2
        # Calculate f(x_n)
        fx_n = f(x_n)
        # Print row
        print(f"{i}\t{a:.6f}\t{b:.6f}\t{x_n:.6f}\t{fx_n:.6f}")
        # Update interval
        if f(a) * fx_n < 0:
            b = x_n
        else:
            a = x_n
    print("-" * 65)
    print(f"Approximate Root: x ≈ {x_n:.6f}")
    return x_n
# Main program
if __name__ == "__main__":
    a = 2 # Lower bound
    b = 4 # Upper bound
    n = 10 # Number of iterations
    root = bisection_method(a, b, n)