'''Problem Statement: 
    You are given n jobs, where each job j ihas a deadline d
    and a profit p. The task is to schedule the jobs such that the total profit is 
    maximized and no two jobs overlap in terms of scheduling time. 
    Each job takes exactly one unit of time, and a job can only be scheduled if its
    deadline is greater than or equal to the current time slot.

Input:

    An array of jobs, where each job has a deadline and profit.
Output:
    The sequence of jobs that maximizes total profit.'''

class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs, t):
    # Sort jobs by profit in descending order
    jobs = sorted(jobs, key=lambda x: x.profit, reverse=True)

    # To keep track of free time slots
    result = [None] * t
    slot = [False] * t
    
    # Iterate through all jobs
    for job in jobs:
        # Find a free slot for this job (starting from the last possible slot)
        for j in range(min(t, job.deadline) - 1, -1, -1):
            if not slot[j]:
                slot[j] = True
                result[j] = job.job_id
                break
    
    # Return the sequence of jobs and the total profit
    return result

# Example
jobs = [Job('J1', 2, 100), Job('J2', 1, 19), Job('J3', 2, 27), Job('J4', 1, 25), Job('J5', 3, 15)]
time_slots = 3  # Maximum time slots
scheduled_jobs = job_scheduling(jobs, time_slots)
print(f"Scheduled Jobs: {scheduled_jobs}")
