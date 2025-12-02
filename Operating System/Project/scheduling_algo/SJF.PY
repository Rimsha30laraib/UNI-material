def SJF():
    # Input section
    num_process = int(input("Enter the number of processes: "))  # Get the number of processes
    Arrival_Time = []
    Execution_Time = []
    
    # Collecting arrival time and execution time for each process
    for i in range(num_process):
        print(f"Enter the details of P{i}:")
        Arrival = int(input("Enter Arrival Time: "))
        Execution = int(input("Enter Execution Time: "))
        Arrival_Time.append(Arrival)
        Execution_Time.append(Execution)

    # Initialize lists for start time, completion time, turnaround time, and waiting time
    Start_Time = [0] * num_process
    Finish_Time = [0] * num_process
    Turnaround_Time = [0] * num_process
    Waiting_Time = [0] * num_process
    Utilization = [0]*num_process

    # Sort processes by execution time (if multiple processes arrive simultaneously, shortest job runs first)
    process_order = sorted(range(num_process), key=lambda i: (Arrival_Time[i], Execution_Time[i]))

    # Calculate start time, completion time, etc.
    current_time = 0
    for i in process_order:
        # Start time is either the current time or the arrival time, whichever is greater
        Start_Time[i] = max(current_time, Arrival_Time[i])
        # Completion time is the start time + execution time
        Finish_Time[i] = Start_Time[i] + Execution_Time[i]
        # Turnaround time is completion time - arrival time
        Turnaround_Time[i] = Finish_Time[i] - Arrival_Time[i]
        # Waiting time is turnaround time - execution time
        Waiting_Time[i] = Turnaround_Time[i] - Execution_Time[i]

        Utilization[i]=Execution_Time[i]/Turnaround_Time[i]
        # Update current time to the completion time of the current process
        current_time = Finish_Time[i]

    # Print the results
    print("\nP\tAT\tET\tST\tFT\tTAT\tWT\tUti")
    for i in range(num_process):
        print(f"P{i}\t{Arrival_Time[i]}\t{Execution_Time[i]}\t{Start_Time[i]}\t{Finish_Time[i]}\t{Turnaround_Time[i]}\t{Waiting_Time[i]}\t{Utilization[i]}")
    
    print("\nGantt Chart:")
    current_time = 0
    print("|", end="")
    for i in process_order:
        start = max(current_time, Arrival_Time[i])
        # Print idle time (if there's any gap between current_time and process start time)
        if start > current_time:
            idle_time = start - current_time
            for _ in range(idle_time):
                print(" 0 |", end="")
        # Print process execution
        for _ in range(Execution_Time[i]):
            print(f" P{i} |", end="")
        # Update current time to the finish time of the process
        current_time = start + Execution_Time[i]
    print("\n")

# Call the function to test
SJF()
