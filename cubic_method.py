import numpy as np

def natural_cubic_spline(x, y):
    n = len(x)
    h = np.diff(x)
    
    alpha = np.zeros(n)
    for i in range(1, n-1):
        alpha[i] = 3 * (y[i+1] - y[i]) / h[i] - 3 * (y[i] - y[i-1]) / h[i-1]
    
    l = np.zeros(n)
    mu = np.zeros(n)
    z = np.zeros(n)
    l[0] = 1
    mu[0] = 0
    z[0] = 0
    
    for i in range(1, n-1):
        l[i] = 2 * (x[i+1] - x[i-1]) - h[i-1] * mu[i-1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i-1] * z[i-1]) / l[i]
    
    l[n-1] = 1
    z[n-1] = 0
    c = np.zeros(n)
    b = np.zeros(n)
    d = np.zeros(n)
    
    for j in range(n-2, -1, -1):
        c[j] = z[j] - mu[j] * c[j+1]
        b[j] = (y[j+1] - y[j]) / h[j] - h[j] * (c[j+1] + 2 * c[j]) / 3
        d[j] = (c[j+1] - c[j]) / (3 * h[j])
    
    return b, c, d

def evaluate_spline(x, x_interp, y, b, c, d):
    n = len(x)
    m = len(x_interp)
    y_interp = np.zeros(m)
    
    for i in range(m):
        for j in range(n-1):
            if x_interp[i] >= x[j] and x_interp[i] <= x[j+1]:
                y_interp[i] = y[j] + b[j] * (x_interp[i] - x[j]) + c[j] * (x_interp[i] - x[j])**2 + d[j] * (x_interp[i] - x[j])**3
    return y_interp

# Given data points
x = np.array([1.2, 1.3, 1.4, 1.5, 1.6])
y = np.array([1.5095, 1.6984, 1.9043, 2.1293, 2.3756])

# Calculate coefficients for natural cubic spline
b, c, d = natural_cubic_spline(x, y)

# Points to interpolate
x_interp = np.array([1.47, 1.67])

# Evaluate the spline at the interpolation points
y_interp = evaluate_spline(x, x_interp, y, b, c, d)

for i in range(len(x_interp)):
    print(f"The approximation at x={x_interp[i]} is: {y_interp[i]}")