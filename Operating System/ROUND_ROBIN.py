import random

class Process:
    def __init__(self, PN, PC, IR, AT, ET, State, SA, PSRI, PSRA, i, resource_info=None, resource_index=None):
        self.PN = PN  #Program Name
        self.PC = PC  # Program Counter
        self.IR = IR  #Instruction register
        self.AT = AT #arrival time
        self.ET = ET  # Execution Time
        self.State = State #state i.e: running/waiting
        self.SA = SA #scheduling algorithm
        #Program Status Word
        self.PSRI = PSRI  # Process State Register Instruction
        self.PSRA = PSRA  # Process State Register Address
        self.i = i  #index
        self.remaining_time = ET #execution time
        self.resume_index = 0  # To keep track of where to resume execution
        self.resource_info = resource_info #i.e: 1 if yes and 0 if no
        self.resource_index = resource_index # the particular index of the process at which the resource is required

#for printing 
    def print_pcb(self):
        print(f"Process Control Block : {self.PN}")
        print(f"Process Id : {self.PN}")
        print(f"Program Counter : {self.PC}")
        print(f"Instruction Register: {self.IR}")
        print(f"Arrival Time : {self.AT}")
        print(f"Execution Time : {self.ET}")
        print(f"Resource Info : {self.resource_info}")
        print(f"State : {self.State}")
        print(f"Scheduling Algorithm: {self.SA}")
        print(f"PSW (Resume Instruction) : {self.PSRI}")
        print(f"PSW (Resume Instruction Address) : {self.PSRA}\n")

#function for running a process 
    def run(self, quantum_size, Process_Ins):
        #if there is any element left to be executed (Remaining time that is the size of the array)
        if self.remaining_time > 0:
            # if we have more than quantum size elements left it will run element according to the quatum size 
            # and if the quantum size is greater and element arae less than elements will be excuted 
            executed_time = min(quantum_size, self.remaining_time)
            start_index = self.resume_index
            end_index = start_index + executed_time
            
            #take the elements and add them to the array for printing
            executed_elements = arrays[self.i][start_index:end_index]
            Process_Ins.extend(executed_elements)
            #calculating the remaining time by subtracting the end from the start to get the total number of elements executed
            self.remaining_time -= (end_index - start_index)
            # resume from where you left last
            self.resume_index = end_index

            #calculate PSRI and PSRA
            self.PSRI = arrays[self.i][self.resume_index - 1] if self.resume_index > 0 else 0
            self.PSRA = self.resume_index - 1
            
            #print the PCB for the executed process
            self.print_pcb()
            #list of the executed processes
            print(f"Process_Ins : {Process_Ins}")

            #handling the resource info thing
            if self.resource_info == 1 and self.resume_index >= self.resource_index:
                #making an array to store the waiting processes                
                waiting_process_info[self.PN] = arrays[self.i][self.resume_index:].copy()  
                # update the state to waiting
                self.State = "Waiting"
                # remaining time set to 0 to freeze the process
                self.remaining_time = 0

# making a class for every process
def create_process_class(PN, PC, IR, AT, ET, State, SA, PSRI, PSRA, i, resource_info=None, resource_index=None):
    class CustomProcess(Process):
        def __init__(self):
            super().__init__(PN, PC, IR, AT, ET, State, SA, PSRI, PSRA, i, resource_info, resource_index)
    return CustomProcess

# Input section
# give the number of processes
num_arrays = int(input("Enter the number of arrays you want to create (must be less than or equal to 5): "))
#enter the quantum size
quantum_size = int(input("Enter quantum size (must be less than or equal to 3): "))
# if quantum size is greater than 3 it will keep on asking again and again
while quantum_size > 3:
    print("Size must be less than or equal to 3. Please try again.")
    quantum_size = int(input("Enter quantum size: "))

#to store the processes
arrays = []
for i in range(num_arrays):
    # to give the size of individual array 
    execution_time = int(input(f"Enter the size of array {i + 1} (must be less than or equal to 10): "))
    #it must be less than or equal to 0
    while execution_time > 10:
        print("Size must be less than or equal to 10. Please try again.")
        execution_time = int(input(f"Enter the size of array {i + 1} (must be less than or equal to 10): "))
    #generate the random numbers 
    array = [random.randint(0, 100) for _ in range(execution_time)]
    # appending the array of process to the main array
    arrays.append(array)

# to print the input in the form of a table
def print_table():
    headers = ["Process", "Execution", "Arrival"]
    print(f"{headers[0].ljust(10)}| {headers[1].ljust(15)}| {headers[2].ljust(7)}")
    print("-" * 35)
    for idx, array in enumerate(arrays, 1):
        process_name = f"P{idx - 1}:{array}"
        execution = str(len(array))
        arrival = str(idx - 1)
        print(f"{process_name.ljust(10)}| {execution.ljust(15)}| {arrival.ljust(7)}")

#call the function
print_table()

processes = [] # for printing the pcb
waiting_process_info = {}  # to store the info of freezed processes
Process_Ins = [] # to store the excuted processes 

# Creating processes
for i in range(num_arrays):
    #values assign
    PN = f"P{i}"
    PC = f"P{i+1}[{i}]"
    IR = f"P{i+1}[{i}]"
    AT = i
    ET = len(arrays[i])
    State = "Running"
    SA = "Round Robin"
    PSRI = 0
    PSRA = 0

    # if the process require resource
    resource_info = int(input(f"Enter resource info for process {PN} (enter 0 if none): "))
    resource_index = None
    if resource_info != 0:
        resource_index = int(input(f"Enter the index where the resource is added for process {PN}: "))

    # creating pcb for every process
    process_class = create_process_class(PN, PC, IR, AT, ET, State, SA, PSRI, PSRA, i, resource_info, resource_index)
    process_instance = process_class()
    #maintaining the classes for every process
    processes.append(process_instance)

# Main loop
process_index = 0  # initialize with the first process

#loop until the array have elements
while any(p.remaining_time > 0 for p in processes):
    current_process = processes[process_index]
    # if the process not require resource run it in the flow
    if current_process.State != "Waiting":  
        current_process.run(quantum_size, Process_Ins)

    # to the next process
    # taking % to go to the same process if there are more elements
    process_index = (process_index + 1) % num_arrays

# handling freezed processes if any
if waiting_process_info:
    waiting_process_names = list(waiting_process_info.keys())
    
    for index, process_name in enumerate(waiting_process_names):
        #the remaining process value to be executed
        values = waiting_process_info[process_name]
        # next process name for ir and pc
        next_process_name = waiting_process_names[(index + 1) % len(waiting_process_names)]  
        #process instance
        waiting_process = Process(
            PN=process_name,  
            PC=next_process_name,  
            IR=next_process_name,  
            AT=0,  
            ET=len(values),  
            State="Running",
            SA="Round Robin",
            PSRI=values[0] if values else 0, 
            PSRA=0,  
            i=processes.index(current_process),  
            resource_info=1,  
        )

        #how many instructions are left
        waiting_process.remaining_time = len(values)
        #to start from the beginnning
        waiting_process.resume_index = 0

        # execute the freezed processes until there are elements
        while waiting_process.remaining_time > 0:
            executed_time = min(quantum_size, waiting_process.remaining_time)

            #starting from where we left
            start_index = waiting_process.resume_index
            end_index = start_index + executed_time

            #don't exceed the length 
            if end_index > len(values):
                end_index = len(values)

            #the executed elements record
            executed_elements = values[start_index:end_index]
            #for printing
            Process_Ins.extend(executed_elements)

            #updating the remaining elements
            waiting_process.remaining_time -= (end_index - start_index)
            waiting_process.resume_index = end_index

            #PSRI and PSRA
            waiting_process.PSRI = values[waiting_process.resume_index - 1] if waiting_process.resume_index > 0 else 0
            waiting_process.PSRA = waiting_process.resume_index - 1

            # printing the pcb
            waiting_process.print_pcb()
            print(f"Process_Ins : {Process_Ins}")
    
    print("All processes completed execution.")
