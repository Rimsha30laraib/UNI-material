def HRRN():
    num_process = int(input("Enter number of processes: "))

    Arrival_Time = []
    Execution_Time = []
    for i in range(num_process):
        print(f"Enter the details of p{i}")
        Arrival = int(input("Enter Arrival Time: "))
        Execution = int(input("Enter Execution Time: "))
        Arrival_Time.append(Arrival)
        Execution_Time.append(Execution)

    # Step 3: Keep track of when each friend starts, finishes, and waits
    Start_Time = [0] * num_process
    Finish_Time = [0] * num_process
    Wait_Time = [0] * num_process
    TurnAround_Time = [0] * num_process
    Utilization = [0] * num_process
    Wait_Time = [0] * num_process

    # Step 4: A list to keep track of which friends have Executioned
    Finished = [False] * num_process
    current_time = 0
    finished_process = 0
    gantt_chart=[]
    # Step 5: Let friends Execution until everyone has Executioned
    while finished_process < num_process:
        max_response_ratio = -1
        next_process = -1

        # Step 6: Find the friend with the highest response ratio
        for i in range(num_process):
            if Arrival_Time[i] <= current_time and not Finished[i]:
                wait_time = current_time - Arrival_Time[i]
                response_ratio = (wait_time + Execution_Time[i]) / Execution_Time[i]

                if response_ratio > max_response_ratio:
                    max_response_ratio = response_ratio
                    next_process = i

         # Step 7: If no process is ready, move the time forward (CPU is idle)
        if next_process == -1:
            gantt_chart.append("0")  # Idle time represented by "0"
            current_time += 1
            continue

        # Step 8: Let the selected friend Execution
        Start_Time[next_process] = current_time
        Finish_Time[next_process] = current_time + Execution_Time[next_process]
        Wait_Time[next_process] = Start_Time[next_process] - Arrival_Time[next_process]
        TurnAround_Time[next_process]=Finish_Time[next_process]-Arrival_Time[next_process]
        Utilization[next_process]=TurnAround_Time[next_process]/Execution_Time[next_process]

        # Add process execution to the Gantt chart
        gantt_chart.extend([f"P{next_process}"] * Execution_Time[next_process])
        current_time = Finish_Time[next_process]

        # Mark the friend as finished
        Finished[next_process] = True
        finished_process += 1

    # Step 9: Show when each friend Executioned and how long they waited
    print("\nP\tAT\tET\tST\tFT\tTAT\tWT\tUti")
    for i in range(num_process):
        print(f"P{i}\t{Arrival_Time[i]}\t{Execution_Time[i]}\t{Start_Time[i]}\t{Finish_Time[i]}\t{TurnAround_Time[i]}\t{Wait_Time[i]}\t{Utilization[i]:.2f}")
    
    # Gantt Chart display
    print("\nGantt Chart:")
    print("|", end="")
    for i in gantt_chart:
        print(f" {i} |", end="")
    print("\n")

# Run the game
HRRN()
