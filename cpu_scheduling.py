# CPU SCHEDULING (FCFS)
# FOLLOWING THE FIRST COME FIRST SERVE (FCFS) ALGORITHM, THE PROCESS THAT ARRIVES FIRST GETS EXECUTED FIRST. 
# A STEP BY STEP EXAMPLE OF THE FCFS ALGORITHM IS SHOWN BELOW. BY SIR EDISON FERANIL

# 1. Define Data
processes = ["P1", "P2", "P3", "P4", "P5"]
arrival_time = [0, 1, 2, 3, 4]
burst_time = [5, 3, 1, 2, 4]

# 2. Prepare variables
n = len(processes)
completion_time = [0] * n
turnaround_time = [0] * n
waiting_time = [0] * n

# 3. Initialize current time
current_time = 0

# 4. simulate FCFS scheduling
for i in range(n):
    # 5. Check CPU idle. If the process arrives after the current time, move the current time to the arrival time
    if arrival_time[i] > current_time:
        current_time = arrival_time[i]
    
    # 6. Calculate completion time
    completion_time[i] = current_time + burst_time[i]
    
    # 7. Calculate turnaround time
    turnaround_time[i] = completion_time[i] - arrival_time[i]
    
    # 8. Calculate waiting time
    waiting_time[i] = turnaround_time[i] - burst_time[i]
    
    # 9. Update current time to the completion time of the current process
    current_time = completion_time[i]
    
# 10. Print results
print("P\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):  
    print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")
    