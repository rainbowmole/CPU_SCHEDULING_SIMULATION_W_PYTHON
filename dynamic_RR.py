#In this activity, we will try to simulate the Round Robin (RR) scheduling algorithm
# CPU SCHEDULING (RR) - DYNAMIC VERSION
# Objective:
# 1. Allow the user to input the number of processes.
# 2. Allow the user to input the arrival time and burst time for each process.
# 3. Allow the user to input the time quantum for the Round Robin scheduling algorithm.
# 4. Implement the RR scheduling algorithm to calculate completion time, turnaround time, and waiting time for each process.

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

# 4. Get time quantum from the user
print()
time_quantum = int(input("\nEnter time quantum: "))

# 4. Prepare variables for scheduling
completion_time = [0] * n
turnaround_time = [0] * n
waiting_time = [0] * n
remaining_time = burst_time[:]  # Copy of burst time to keep track of remaining time for each process
is_in_queue = [False] * n

# 5. Initialize current time
current_time = 0
completed = 0
queue = [] # Queue to hold processes that are ready to execute

# 6. add processes that have arrived at time 0 to the queue
for i in range(n):
    if arrival_time[i] == 0:
        queue.append(i)
        is_in_queue[i] = True

# 7. Simulate RR scheduling
while completed < n:
    
    if len(queue) == 0:
        # If no processes are in the queue, move to the next time unit
        current_time += 1
        # Check for newly arrived processes
        for i in range(n):
            if arrival_time[i] == current_time and not is_in_queue[i]:
                queue.append(i)
                is_in_queue[i] = True
        continue
    
    # Get the index of the process at the front of the queue
    i = queue.pop(0)
    
    run_time = min(time_quantum, remaining_time[i])
    current_time += run_time
    remaining_time[i] -= run_time
    
    # check in any new process has arrived during the execution of the current process
    for j in range(n):
        if arrival_time[j] <= current_time + time_quantum and not is_in_queue[j]:
            queue.append(j)
            is_in_queue[j] = True
    
    # Execute the process for a time quantum or until it finishes, whichever comes first
    if remaining_time[i] == 0:
        #process is already completed
        # 10. Calculate completion time
        completion_time[i] = current_time
        # 11. Calculate turnaround time
        turnaround_time[i] = completion_time[i] - arrival_time[i]       
        # 12. Calculate waiting time
        waiting_time[i] = turnaround_time[i] - burst_time[i]
        completed += 1
    else:
        queue.append(i) # re-add the process to the end of the queue for the next round of execution

print("\nP\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")