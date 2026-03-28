	CPU SCHEDULING SIMULATION PROJECT TO UNDERSTAND BETTER HOW CPU SCHEDULING WORKS

	NOTE: 
        THIS IS A SCHOOL PROJECT
		Codes from cpu_scheduling came from my professor
		Dynamic codes are modified version of the given code

	KEY DESCRIPTIONS OF EACH CODE
	‣ cpu_scheduling.py 
	
	        A hardcoded First Come First Serve Algorithm
	
	‣ dynamic_FCFS.py
	
	        A modified version of cpu_scheduling.py 
			
	        Users are able to input:
	          - number of processes
	          - arrival time 
	          - burst time
	
	‣ dynamic_SJF.py
	
	        Tried a different approach of cpu scheduling
	        Implemented a Shortest Job First Algorithm
			
	        Users are able to input:
	          - number of processes
	          - arrival time
	          - burst time

	‣ dynamic_RR.py

			Another aproach of cpue scheduling
			Implemented the Round Robin Algorithm to 
			understand further cpu scheduling with quantums

			Users are able to input:
				- number of processes
				- arrival time
				- burst time
				- quantum

			Key takeaways from this code:
			- quantum is a fixed time slice
			- instead of picking the shortest job or following the order of processes, 
			  it picks whoever next in the queue, making it preemptive(allowing a process 
			  to be interrupted and move to the ready state.)
			
