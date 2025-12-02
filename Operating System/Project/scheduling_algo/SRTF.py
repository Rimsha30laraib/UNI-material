# def SRTF():
#     # Input section
#     num_process = int(input("Enter the number of processes: "))  # Get the number of processes
#     Arrival_Time = []
#     Execution_Time = []
    
#     # Collecting arrival time and execution time for each process
#     for i in range(num_process):
#         print(f"Enter the details of P{i}:")
#         Arrival = int(input("Enter Arrival Time: "))
#         Execution = int(input("Enter Execution Time: "))
#         Arrival_Time.append(Arrival)
#         Execution_Time.append(Execution)

#     # Remaining execution times (initially the same as execution times)
#     Remaining_Time = Execution_Time[:]

#     # Initialize variables
#     current_time = 0
#     completed = 0
#     min_remaining_time = float('inf')
#     shortest = 0
#     finish_time = 0
#     is_completed = [False] * num_process


#     Start_Time = [0]*num_process
#     Waiting_Time = [0] * num_process
#     Turnaround_Time = [0] * num_process
#     Finish_Time = [0] * num_process
#     Utilization = [0]*num_process
#     # Loop until all processes are completed
#     while completed != num_process:
#         # Find the process with the shortest remaining time at the current time
#         for i in range(num_process):
#             if Arrival_Time[i] <= current_time and not is_completed[i] and Remaining_Time[i] < min_remaining_time and Remaining_Time[i] > 0:
#                 min_remaining_time = Remaining_Time[i]
#                 shortest = i

#         if min_remaining_time == float('inf'):
#             current_time += 1
#             continue

#         # Decrement the remaining time of the current shortest process
#         Remaining_Time[shortest] -= 1
#         min_remaining_time = Remaining_Time[shortest]

#         if Remaining_Time[shortest] == 0:
#             # If the process is completed, record the finish time
#             completed += 1
#             is_completed[shortest] = True
#             finish_time = current_time + 1
#             Finish_Time[shortest] = finish_time

#             # Calculate turnaround and waiting time for the completed process
#             # Start_Time[shortest] = current_time
#             # if Start_Time[shortest] == -1:  # If the process has not started yet
#             #     Start_Time[shortest] = current_time  # Set start time when it first starts

#             Turnaround_Time[shortest] = Finish_Time[shortest] - Arrival_Time[shortest]
#             Waiting_Time[shortest] = Turnaround_Time[shortest] - Execution_Time[shortest]
#             Utilization[shortest]=Execution_Time[shortest]/Turnaround_Time[shortest]
#             if Waiting_Time[shortest] < 0:
#                 Waiting_Time[shortest] = 0

#         current_time += 1
#         min_remaining_time = float('inf')

#     # Print the results
#     print("\nP\tAT\tET\tST\tFT\tTAT\tWT\tUti")
#     for i in range(num_process):
#         print(f"P{i}\t{Arrival_Time[i]}\t{Execution_Time[i]}\t{Start_Time[i]}\t{Finish_Time[i]}\t{Turnaround_Time[i]}\t{Waiting_Time[i]}\t{Utilization[i]}")
    
#     print("\nGantt Chart:")
#     current_time = 0
#     print("|", end="")
#     for i in num_process:
#         start = max(current_time, Arrival_Time[i])
#         # Print idle time (if there's any gap between current_time and process start time)
#         if start > current_time:
#             idle_time = start - current_time
#             for _ in range(idle_time):
#                 print(" 0 |", end="")
#         # Print process execution
#         for _ in range(Execution_Time[i]):
#             print(f" P{i} |", end="")
#         # Update current time to the finish time of the process
#         current_time = start + Execution_Time[i]
#     print("\n")
# # Call the function
# SRTF()


def SRTF():
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

    # Remaining execution times (initially the same as execution times)
    Remaining_Time = Execution_Time[:]

    # Initialize variables
    current_time = 0
    completed = 0
    min_remaining_time = float('inf')
    shortest = 0
    finish_time = 0
    is_completed = [False] * num_process
    is_started = [False] * num_process  # To track if a process has started

    Start_Time = [-1] * num_process  # Initialize to -1, meaning not yet started
    Waiting_Time = [0] * num_process
    Turnaround_Time = [0] * num_process
    Finish_Time = [0] * num_process
    Utilization = [0] * num_process

    gantt_chart = []

    # Loop until all processes are completed
    while completed != num_process:
        # Find the process with the shortest remaining time at the current time
        for i in range(num_process):
            if Arrival_Time[i] <= current_time and not is_completed[i] and Remaining_Time[i] < min_remaining_time and Remaining_Time[i] > 0:
                min_remaining_time = Remaining_Time[i]
                shortest = i

        if min_remaining_time == float('inf'):  # No process is ready to execute, so CPU is idle
            gantt_chart.append("0")  # Represent idle time with "0"
            current_time += 1
            continue

        # If the process is starting for the first time, record its start time
        if not is_started[shortest]:
            Start_Time[shortest] = current_time
            is_started[shortest] = True

        # Decrement the remaining time of the current shortest process
        Remaining_Time[shortest] -= 1
        gantt_chart.append(f"P{shortest}")  # Add process execution to Gantt chart

        if Remaining_Time[shortest] == 0:
            # If the process is completed, record the finish time
            completed += 1
            is_completed[shortest] = True
            finish_time = current_time + 1
            Finish_Time[shortest] = finish_time

            # Calculate turnaround and waiting time for the completed process
            Turnaround_Time[shortest] = Finish_Time[shortest] - Arrival_Time[shortest]
            Waiting_Time[shortest] = Turnaround_Time[shortest] - Execution_Time[shortest]
            Utilization[shortest] = Execution_Time[shortest] / Turnaround_Time[shortest]

            if Waiting_Time[shortest] < 0:
                Waiting_Time[shortest] = 0

        current_time += 1
        min_remaining_time = float('inf')

    # Print the results
    print("\nP\tAT\tET\tST\tFT\tTAT\tWT\tUti")
    for i in range(num_process):
        print(f"P{i}\t{Arrival_Time[i]}\t{Execution_Time[i]}\t{Start_Time[i]}\t{Finish_Time[i]}\t{Turnaround_Time[i]}\t{Waiting_Time[i]}\t{Utilization[i]:.2f}")
    
    # Gantt Chart display
    print("\nGantt Chart:")
    print("|", end="")
    for i in gantt_chart:
        print(f" {i} |", end="")
    print("\n")


# Call the function
SRTF()
