#In this activity, we will try to simulate the Shortest Job First (SJF) scheduling algorithm
# CPU SCHEDULING (SJF) - DYNAMIC VERSION
# Objective:
# 1. Allow the user to input the number of processes.
# 2. Allow the user to input the arrival time and burst time for each process.
# 3. Implement the SJF scheduling algorithm to calculate completion time, turnaround time, and waiting time for each process.

# 1. Get the number of processes from the user
n = int(input("Enter the number of processes: "))
                                                                
# 2. Initialize lists to store process information                      
processes = []
arrival_time = []
burst_time = []

# 3. Get process information from the user
for i in range(n):
    process_name = (f"P{i + 1}")
    print()
    at = int(input(f"Enter {process_name}'s arrival time:  "))
    bt = int(input(f"Enter {process_name}'s burst time:    "))
    
    processes.append(process_name)
    arrival_time.append(at)
    burst_time.append(bt)
    
# 4. Prepare variables for scheduling
completion_time = [0] * n
turnaround_time = [0] * n
waiting_time = [0] * n
is_completed = [False] * n

# 5. Initialize current time
current_time = 0
completed = 0

# 6. Simulate SJF scheduling
while completed < n:
    
    # 7. Find all processes that have arrived and are not yet completed
    Avialable_processes = []
    for i in range(n):
        if arrival_time[i] <= current_time and not is_completed[i]:
            Avialable_processes.append(i)
            
    if len(Avialable_processes) == 0:
        # If no processes are available, move to the next time unit
        current_time += 1
        continue
    
    # 8. Among the available processes, find the one with the shortest burst time
    shortest_job_index = Avialable_processes[0]
    for i in Avialable_processes:
        if burst_time[i] < burst_time[shortest_job_index]:
            shortest_job_index = i
    
    # 9. Execute the shortest job
    i = shortest_job_index
    # 10. Calculate completion time
    completion_time[i] = current_time + burst_time[i]
    # 11. Calculate turnaround time
    turnaround_time[i] = completion_time[i] - arrival_time[i]       
    # 12. Calculate waiting time
    waiting_time[i] = turnaround_time[i] - burst_time[i]
    # 13. Mark the process as completed
    current_time = completion_time[i]
    is_completed[i] = True
    completed += 1
    
# 14. print results
print("\nP\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")
    
    