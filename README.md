# Algorithms

Implementations of and explanations for a number of Algorithms.

## Complexity

For a given algorithm, the time taken to execute it and the size of data input it receives determine its efficiency.

- Space Complexity is the amount of memory space the algorithm requires for its life cycle.
  - Consider space for storing data and variables (even constants), irregardless of the `problem size`. Even the program size falls here.
  - Consider dynamic memory allocation, space taken by the stack during recursion. This is variable; the size of variables depends on the `problem size`.
  - The formula for Space Complexity (SC) of an Algorithm (A) can be represented as `SC(A) = F + SC(I)`
  - F is the fixed part of the algorithm whereas V is the variable part (dependant on characteristics therein).

- Time Complexity is the amount of time the algorithm requires to run from start to finish.
  - The formula used for this time requirement can be represented as `T(n) = c * n` for a program of input size `n`.

## Problem Solving Approaches

- `Divide and conquer`: Split a problem into sub-problems, break these further to the smallest possible, then solve and merge them into the final solution.
- `Divide/Break`: This is recursive in nature in that the problem is broken into smaller sub-problems (that represent a portion/part of the original) until no further representations can be made.
- `Conquer/Solve`: Take in small sub-problems to be solved. These problems are basically already solved on their own.
- `Merge/Combine`: Recursively combine the solved sub-problems (from `Conquer/Solve`) into the solution of the original problem.

## Python

1. [Binary Search](Python/binary_search.py) or implementation [as a class](https://github.com/Rwothoromo/andela_labs/blob/master/binary_search/binary_search.py).
