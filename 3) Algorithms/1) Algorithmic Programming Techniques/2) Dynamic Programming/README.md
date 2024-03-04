# Dynamic Programming

> Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems and solving each subproblem only once.
> <br/>
> <br/>
> Unlike other problem-solving techniques that may solve the same subproblem multiple times, dynamic programming stores the solutions to subproblems in a table and reuses them when needed. This results in significant time and space savings, making dynamic programming an efficient approach for solving optimization problems.

<br/>


## How Does Dynamic Programming Work?

At the heart of dynamic programming is the concept of memoization, which involves storing the results of solved subproblems in a table (usually an array or a matrix) and retrieving them when needed. By avoiding redundant computations, dynamic programming algorithms achieve optimal solutions to complex problems with improved time and space complexity.

<br/>




## Key Components of Dynamic Programming:

1. **Optimal Substructure:** A problem exhibits optimal substructure if an optimal solution to the problem can be constructed from optimal solutions to its subproblems. Dynamic programming exploits this property by breaking down the problem into smaller subproblems and combining their solutions to find the overall optimal solution.

2. **Overlapping Subproblems:** A problem exhibits overlapping subproblems if it can be broken down into smaller subproblems that are reused multiple times. Dynamic programming leverages this property by storing the solutions to subproblems in a table and reusing them when needed, eliminating redundant computations.

<br/>



## Example of Dynamic Programming:

```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        memo = [0] * (n + 1)
        memo[1] = 1
        for i in range(2, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n]

# Calculate the 10th Fibonacci number
result = fibonacci(10)
print("10th Fibonacci number:", result)
```

In this example, the fibonacci function calculates the nth Fibonacci number using dynamic programming. It stores the results of solved subproblems in the memo table and retrieves them when needed to avoid redundant computations.

<br/>



## Why Use Dynamic Programming?
Dynamic programming offers several advantages in solving optimization problems, including:

* Efficiency: By storing the solutions to subproblems and reusing them when needed, dynamic programming algorithms achieve optimal solutions with improved time and space complexity.
* Simplicity: Dynamic programming provides a structured and systematic approach to solving complex problems, making it easier to understand and implement.
* Versatility: Dynamic programming can be applied to a wide range of optimization problems, including sequence alignment, shortest path problems, knapsack problems, and more.
