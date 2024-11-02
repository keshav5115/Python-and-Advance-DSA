'''
A greedy algorithm is an approach to problem-solving that makes a 
series of choices, each of which is the best or most optimal at 
that moment, with the hope that these local optima will lead to 
a globally optimal solution.
'''








'''
Activity Selection Problem
Problem Statement: 
    Given n activities with their start and finish times, 
    select the maximum number of activities that can be performed
    by a single person, assuming that a person can only work on a 
    single activity at a time.

Input:

    Two arrays: start[] and finish[], which contain 
    the start and finish times of n activities.
Output:

    The maximum number of activities that can be selected such that
    no two selected activities overlap.

    '''
def activity_selection(start, finish):
    n = len(finish)
    # Sort activities by finish time
    activities = sorted(zip(start, finish), key=lambda x: x[1])
    
    # The first activity is always selected
    selected_activities = [0]
    last_finish_time = activities[0][1]
    
    # Iterate through remaining activities
    for i in range(1, n):
        if activities[i][0] >= last_finish_time:
            selected_activities.append(i)
            last_finish_time = activities[i][1]
    
    return selected_activities

# Example
start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
selected = activity_selection(start, finish)
print(f"Selected activities: {selected}")

'''
Coin Change Problem 
Problem Statement: Given a value V and a set of denominations of 
coins, find the minimum number of coins that sum up to the given 
value V. Assume you have an unlimited supply of each denomination.

Input:

    A value V.
    An array coins[] of available coin denominations.
Output:

    The minimum number of coins needed to make the value V.


'''
def coin_change(coins, V):
    coins.sort(reverse=True)
    result = []
    
    for coin in coins:
        while V >= coin:
            V -= coin
            result.append(coin)
    
    return result

# Example
coins = [1, 5, 10, 25]
value = 63
change = coin_change(coins, value)
print(f"Coins used to make {value}: {change}")


