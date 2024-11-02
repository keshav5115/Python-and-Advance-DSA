

'''
Dynamic Programming is a method for solving complex problems by breaking them down into 
simpler subproblems and solving each subproblem only once, 
storing their solutions (usually in a table) to avoid redundant computations. 
It is particularly useful when the problem has overlapping subproblems and an optimal
substructure.


'''
from time import time
# using recursive programming

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)
'''
exponential time complexity O(2^n).
'''
# using Dynamic Programming

def fibonacci_dp(n):
    # Initialize a table to store Fibonacci values
    fib_table = [0] * (n + 1)
    
    # Base cases
    fib_table[0] = 0
    fib_table[1] = 1
    
    # Fill the table in a bottom-up manner
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
    
    return fib_table[n]
#Dynamic Programming Approach: O(n), as we calculate each Fibonacci number once and 
# store the results.
# Example:

def fib_bottom_up(n):
    num1=0
    num2=1
    if n<=1:
        return n
    for _ in range(2,n+1):
        temp=num1
        num1=num2
        num2=temp+num1
    return num2

start=time()
print(fib_recursive(30))
end=time()
print('recursive_function:-',end-start,'in mili seconds')

start=time()
print(fibonacci_dp(30)) 
end=time()
print('dynamic programming:-',end-start)

