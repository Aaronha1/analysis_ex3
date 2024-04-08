import math

def simpsons_method(f, a, b, n):
    """
    Approximates the integral of a ftion using Simpson's method.

    Parameters:
        f (ftion): The integrand function.
        a (float): The lower limit of integration.
        b (float): The upper limit of integration.
        n (int): The number of subintervals. Must be even.

    Returns:
        float: The approximate value of the integral.
    """
    if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even.")
    
    h = (b - a) / n
    x = [a + i * h for i in range(n+1)]
    
    integral = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            integral += 2 * f(x[i])
        else:
            integral += 4 * f(x[i])
    
    return integral * h / 3


# Example usage:
f = lambda x: math.sin(x ** 2)  # function
a = 0  # Lower limit
b = 1  # Upper limit
n = 4  # Number of subintervals

I = simpsons_method(f, a, b, n)
print("Approximate integral:", I)

