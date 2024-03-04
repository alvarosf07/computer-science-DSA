# Recursion
> Recursion is a programming technique to solve problems by following a **recursive** process, in which a function calls itself a certain amount of times until a base case is reached.
> <br/>
> <br/>
> Instead of solving the entire problem at once, a recursive function breaks it down into smaller, more manageable subproblems and solves each subproblem recursively.

<br/>

## How Does Recursion Work?

At the heart of recursion is the concept of self-reference: a function calls itself with a modified input until it reaches a base case, at which point it returns a result without making any further recursive calls. This process can be visualized as a series of nested function calls, with each call contributing to the solution of the overall problem.

<br/>



## Key Components of Recursion:

1. **Base Case:** A condition that determines when the recursion should stop. It represents the simplest form of the problem that can be solved directly without further recursion.

2. **Recursive Case:** The part of the function that calls itself with a modified input. It breaks down the original problem into smaller subproblems and contributes to the solution by solving each subproblem recursively.

<br/>



## Example of Recursion:

```python
def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: multiply n by factorial of (n-1)
    else:
        return n * factorial(n-1)

# Calculate the factorial of 5
result = factorial(5)
print("Factorial of 5:", result)
```

In this example, the factorial function calculates the factorial of a non-negative integer n. It demonstrates recursion by calling itself with a modified input (n-1) until it reaches the base case (n = 0 or n = 1).

<br/>



## Why Use Recursion?
Recursion is a fundamental concept in computer science and programming that plays a crucial role in solving a wide range of problems.
Recursion offers several advantages in programming, including:

  * Simplicity: Recursive solutions are often more concise and easier to understand than iterative solutions for certain problems.
  * Modularity: Recursion allows complex problems to be broken down into smaller, more manageable subproblems, promoting code reusability and modularity.
  * Elegance: Recursion can lead to elegant and efficient solutions for problems that have a recursive structure, such as tree traversal, graph traversal, and divide-and-conquer algorithms.



