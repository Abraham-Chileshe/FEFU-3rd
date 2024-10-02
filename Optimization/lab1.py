import math

# Define the function
def f(x):
    return x**2 - 3*x + x * math.log(x)

# Dichotomy method
def dichotomy_method(f, a, b, epsilon):
    delta = epsilon / 10
    num_iterations = 0
    while (b - a) > epsilon:
        mid = (a + b) / 2
        x1 = mid - delta
        x2 = mid + delta
        if f(x1) < f(x2):
            b = x2
        else:
            a = x1
        num_iterations += 1
        print(f"Iteration {num_iterations}: x = {(a + b) / 2:.6f}")
    return (a + b) / 2, num_iterations

# Golden section method
def golden_section_method(f, a, b, epsilon):
    phi = (1 + math.sqrt(5)) / 2
    resphi = 2 - phi  # Reciprocal of phi
    num_iterations = 0

    # Initial points
    x1 = a + resphi * (b - a)
    x2 = b - resphi * (b - a)

    while (b - a) > epsilon:
        if f(x1) < f(x2):
            b = x2
            x2 = x1
            x1 = a + resphi * (b - a)
        else:
            a = x1
            x1 = x2
            x2 = b - resphi * (b - a)

        num_iterations += 1
        print(f"Iteration {num_iterations}: x = {(a + b) / 2:.6f}")
    return (a + b) / 2, num_iterations

# Fibonacci method
def fibonacci_method(f, a, b, epsilon):
    # Generate Fibonacci numbers until the ratio is greater than the interval size
    fibs = [1, 1]
    while fibs[-1] < (b - a) / epsilon:
        fibs.append(fibs[-1] + fibs[-2])

    n = len(fibs) - 1
    num_iterations = 0

    # Initial points
    x1 = a + (fibs[n-2] / fibs[n]) * (b - a)
    x2 = a + (fibs[n-1] / fibs[n]) * (b - a)

    for i in range(1, n):
        if f(x1) < f(x2):
            b = x2
            x2 = x1
            x1 = a + (fibs[n-i-2] / fibs[n-i]) * (b - a)
        else:
            a = x1
            x1 = x2
            x2 = a + (fibs[n-i-1] / fibs[n-i]) * (b - a)

        num_iterations += 1
        print(f"Iteration {num_iterations}: x = {(a + b) / 2:.6f}")

    return (a + b) / 2, num_iterations

# Main calculation
a, b = 1, 2
epsilon = 0.005

# Dichotomy method result
print("----------------------------- \n Dichotomy method:\n-----------------------------")
dichotomy_min, iter_dichotomy = dichotomy_method(f, a, b, epsilon)
print(f"Dichotomy method: Minimum at x = {dichotomy_min:.6f} after {iter_dichotomy} iterations\n")

# Golden section method result
print("----------------------------- \n Golden section method: \n-----------------------------")
golden_min, iter_golden = golden_section_method(f, a, b, epsilon)
print(f"Golden section method: Minimum at x = {golden_min:.6f} after {iter_golden} iterations\n")

# Fibonacci method result
print("----------------------------- \n Fibonacci method: \n-----------------------------")
fibonacci_min, iter_fibonacci = fibonacci_method(f, a, b, epsilon)
print(f"Fibonacci method: Minimum at x = {fibonacci_min:.6f} after {iter_fibonacci} iterations")
