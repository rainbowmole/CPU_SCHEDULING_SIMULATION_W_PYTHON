# A challenge activity for CPU scheduling. 
# In this activity, we will modify the existing FCFS Scheduling algorithm to be dynamic, 
# allowing the user to input the number of processes, their arrival times, and burst times.

# CPU SCHEDULING (FCFS) - DYNAMIC VERSION
# Objective:
# 1. Allow the user to input the number of processes.
# 2. Allow the user to input the arrival time and burst time for each process.

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

# 5. Initialize current time
current_time = 0

# 6. Simulate FCFS scheduling
for i in range(n):
    # 7. Check CPU idle. If the process arrives after the current time, move the current time to the arrival time
    if arrival_time[i] > current_time:
        current_time = arrival_time[i]
    
    # 8. Calculate completion time
    completion_time[i] = current_time + burst_time[i]
    
    # 9. Calculate turnaround time
    turnaround_time[i] = completion_time[i] - arrival_time[i]
    
    # 10. Calculate waiting time
    waiting_time[i] = turnaround_time[i] - burst_time[i]
    
    # 11. Update current time to the completion time of the current process
    current_time = completion_time[i]

# 12. Print results
print("\nP\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):  
    print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")
    