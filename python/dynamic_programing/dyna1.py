'''
def is_prime(num):
    flag=True
    for i in range(1,(num//2)+1 ):
        if i==1:
            continue
        if num%i==0:
            flag=False
            break
    return flag

def downToZero(n):
    # Write your code here
    memo=[-1]*(n+1)
    memo[0]=1
    memo[1]=1
    memo[2]=memo[0]+memo[1]
    
   
    for i in range(3,n+1):
        memo[i]=memo[i-1]+1
        if is_prime(i):
            continue
        for j in range(2,i):
            if i%j==0:
                

                memo[i]=min(memo[i],memo[max(j,i//j)]+1)
    print(memo)
    return memo[-1]
'''
from collections import deque
import math
def downToZero(n):
    # Memo array to store minimum steps to reach 0
    memo = [0] * (n + 1)
    memo[0] = 0  # Takes 0 moves to get from 0 to 0

    # Queue for BFS
    queue = deque([n])
    
    while queue:
        curr = queue.popleft()
        
        # If we've reached 0, return the number of moves
        if curr == 0:
            return memo[curr]
        
        # 1. Subtract 1 and move
        if memo[curr - 1] == 0:  # If not visited yet
            memo[curr - 1] = memo[curr] + 1
            queue.append(curr - 1)
        
        # 2. Try all possible divisors of the current number
        for i in range(2, int(math.sqrt(curr)) + 1):
            if curr % i == 0:
                # Both divisors are potential next steps: `i` and `curr // i`
                next_move = max(i, curr // i)
                if memo[next_move] == 0:  # If not visited yet
                    memo[next_move] = memo[curr] + 1
                    queue.append(next_move)
    print(memo)
    return memo[n]

# Example usage:
n = 3  # You can change this value to test
print(downToZero(n))

print(downToZero(5))