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
    
    result=[]
    for i in selected_activities:
        result.append(activities[i])
    return result=


# Example
start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
selected = activity_selection(start, finish)
print(f"Selected activities: {selected}")