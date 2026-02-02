# Bisection Method in Python

This project implements the **Bisection Method**, a numerical algorithm used to find the approximate root of a nonlinear equation of the form:

f(x) = 0

The method works by repeatedly narrowing down an interval that contains the root.

---

## Problem Description

The function solved in this program is:

f(x) = x³ − 2x − 5

Given an interval \([a, b]\) where the function changes sign, the bisection method is applied to approximate the root.

---

## How the Bisection Method Works

1. Select an interval \([a, b]\) such that f(a) × f(b) < 0  
2. Compute the midpoint:

   xₙ = (a + b) / 2

3. Evaluate f(xₙ)
4. Replace either `a` or `b` depending on the sign of f(xₙ)
5. Repeat the process for a fixed number of iterations

---

## Features

- Validates whether the initial interval is suitable
- Displays results in a clear tabular format
- Calculates and prints the approximate root
- Simple and beginner-friendly implementation

---

## How to Run the Program

### Requirements
- Python 3.x

### Steps
1. Clone or download the repository
2. Navigate to the project directory
3. Run the program using:

```bash
python bisection_method.py
```
## Input parameters
```bash
python

a = 2     # Lower bound
b = 4     # Upper bound 
n = 10    # Number of iterations
```
## Output
The program is a table containing:

- Iteration number 
- Lower bound (a)
- Upper bound (b)
- Mid-point (Xn)
- Function value at mid-point(f(Xn))

After all iterations the approximate root is displayed

## Applications
- Learning numerical methods
- Engineering and scientific computations
- Academic demonstrations of root-finding algorithms

## Author 
SUCCESS AKPORUOVO <br>
