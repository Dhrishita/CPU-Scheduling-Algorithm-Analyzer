import tkinter as tk
from tkinter import ttk, messagebox

class CPUSchedulingAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("CPU Scheduling Algorithm Analyzer")

        self.algorithm = tk.StringVar(value="FCFS")
        self.process_data = []
        self.process_entries = []

        # Input Frame
        input_frame = ttk.LabelFrame(self.root, text="Input", padding=10)
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Algorithm Selection
        ttk.Label(input_frame, text="Select Algorithm:").grid(row=0, column=0, sticky="w")
        ttk.Radiobutton(input_frame, text="FCFS (Non-Preemptive)", variable=self.algorithm, value="FCFS").grid(row=0, column=1, sticky="w")
        ttk.Radiobutton(input_frame, text="SJF (Non-Preemptive)", variable=self.algorithm, value="SJF").grid(row=0, column=2, sticky="w")
        ttk.Radiobutton(input_frame, text="Priority (Non-Preemptive)", variable=self.algorithm, value="Priority").grid(row=0, column=3, sticky="w")
        ttk.Radiobutton(input_frame, text="Round Robin (Preemptive)", variable=self.algorithm, value="RR").grid(row=0, column=4, sticky="w")
        ttk.Radiobutton(input_frame, text="SRTF (Preemptive)", variable=self.algorithm, value="SRTF").grid(row=0, column=5, sticky="w")
        ttk.Radiobutton(input_frame, text="Priority (Preemptive)", variable=self.algorithm, value="PriorityPreemptive").grid(row=0, column=6, sticky="w")

        # Number of Processes Entry
        ttk.Label(input_frame, text="Number of Processes:").grid(row=1, column=0, sticky="w")
        self.num_processes_entry = ttk.Entry(input_frame, width=10)
        self.num_processes_entry.grid(row=1, column=1, sticky="w")
        ttk.Button(input_frame, text="Generate Fields", command=self.generate_process_fields).grid(row=1, column=2)

        # Time Quantum Input (for Round Robin)
        self.time_quantum_label = ttk.Label(input_frame, text="Time Quantum:")
        self.time_quantum_label.grid(row=2, column=0, sticky="w")
        self.time_quantum_entry = ttk.Entry(input_frame, width=10)
        self.time_quantum_entry.grid(row=2, column=1, sticky="w")

        # Buttons
        ttk.Button(input_frame, text="Calculate", command=self.calculate).grid(row=3, column=0, pady=10)
        ttk.Button(input_frame, text="Clear", command=self.clear).grid(row=3, column=1, pady=10)

        # Output Frame
        self.output_frame = ttk.LabelFrame(self.root, text="Output", padding=10)
        self.output_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.output_table = ttk.Treeview(self.output_frame, columns=("Process", "AT", "BT", "CT", "TAT", "WT"), show="headings")
        self.output_table.heading("Process", text="Process")
        self.output_table.heading("AT", text="Arrival Time")
        self.output_table.heading("BT", text="Burst Time")
        self.output_table.heading("CT", text="Completion Time")
        self.output_table.heading("TAT", text="Turnaround Time")
        self.output_table.heading("WT", text="Waiting Time")
        self.output_table.pack(fill="both", expand=True)

        # Average Time Labels
        self.avg_tat_label = ttk.Label(self.output_frame, text="Average TAT: ")
        self.avg_tat_label.pack(pady=5)

        self.avg_wt_label = ttk.Label(self.output_frame, text="Average WT: ")
        self.avg_wt_label.pack(pady=5)

    def generate_process_fields(self):
        # Clear any existing process entries
        for widget in self.process_entries:
            widget.destroy()

        self.process_entries = []
        num_processes = self.num_processes_entry.get()
        
        if not num_processes.isdigit() or int(num_processes) <= 0:
            messagebox.showerror("Error", "Please enter a valid number of processes.")
            return

        num_processes = int(num_processes)

        # Grid for Process Input
        grid_frame = ttk.Frame(self.root)
        grid_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(grid_frame, text="Process").grid(row=0, column=0)
        ttk.Label(grid_frame, text="Arrival Time").grid(row=0, column=1)
        ttk.Label(grid_frame, text="Burst Time").grid(row=0, column=2)
        ttk.Label(grid_frame, text="Priority").grid(row=0, column=3)

        for i in range(num_processes):
            entries = []
            ttk.Label(grid_frame, text=f"P{i+1}").grid(row=i+1, column=0)
            for j in range(3):
                entry = ttk.Entry(grid_frame, width=10)
                entry.grid(row=i+1, column=j+1)
                entry.bind("<Left>", lambda event, row=i, col=j: self.move_focus(event, row, col, "left"))
                entry.bind("<Right>", lambda event, row=i, col=j: self.move_focus(event, row, col, "right"))
                entry.bind("<Up>", lambda event, row=i, col=j: self.move_focus(event, row, col, "up"))
                entry.bind("<Down>", lambda event, row=i, col=j: self.move_focus(event, row, col, "down"))
                entries.append(entry)
            self.process_entries.append(entries)
    
    def generate_fields(self):
        # Clear previous process entry fields if any
        for widget in self.process_frame.winfo_children():
            widget.destroy()
        
        # Get number of processes
        try:
            self.num_processes = int(self.num_processes_entry.get())
        except ValueError:
            return  # Exit if input is not an integer
        
        # Create new entry fields for processes
        self.process_entries = []
        for i in range(self.num_processes):
            label = tk.Label(self.process_frame, text=f"Process {i + 1}:")
            label.grid(row=i, column=0, padx=10, pady=5)
            
            arrival_time_entry = tk.Entry(self.process_frame)
            arrival_time_entry.grid(row=i, column=1, padx=10, pady=5)
            
            burst_time_entry = tk.Entry(self.process_frame)
            burst_time_entry.grid(row=i, column=2, padx=10, pady=5)
            
            priority_entry = tk.Entry(self.process_frame)
            priority_entry.grid(row=i, column=3, padx=10, pady=5)
            
            self.process_entries.append((arrival_time_entry, burst_time_entry, priority_entry))

    def move_focus(self, event, row, col, direction):
        if direction == "left" and col > 0:
            self.process_entries[row][col - 1].focus_set()
        elif direction == "right" and col < 3:
            self.process_entries[row][col + 1].focus_set()
        elif direction == "up" and row > 0:
            self.process_entries[row - 1][col].focus_set()
        elif direction == "down" and row < len(self.process_entries) - 1:
            self.process_entries[row + 1][col].focus_set()

    def calculate(self):
        self.process_data = []
        for i, entries in enumerate(self.process_entries):
            try:
                at = int(entries[0].get()) if entries[0].get() else 0
                bt = int(entries[1].get()) if entries[1].get() else 0
                prio = int(entries[2].get()) if entries[2].get() else 0
                self.process_data.append({"pid": f"P{i+1}", "AT": at, "BT": bt, "Priority": prio})
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter integers.")
                return

        algo = self.algorithm.get()
        if algo in ["RR"] and not self.time_quantum_entry.get().isdigit():
            messagebox.showerror("Error", "Please provide a valid Time Quantum.")
            return

        if algo == "RR":
            time_quantum = int(self.time_quantum_entry.get())
            self.process_data = self.round_robin(self.process_data, time_quantum)
        elif algo == "SRTF":
            self.process_data = self.srtf(self.process_data)
        elif algo == "FCFS":
            self.process_data = self.fcfs(self.process_data)
        elif algo == "SJF":
            self.process_data = self.sjf_non_preemptive(self.process_data)
        elif algo == "Priority":
            self.process_data = self.priority_non_preemptive(self.process_data)
        elif algo == "PriorityPreemptive":
            self.process_data = self.priority_preemptive(self.process_data)

        self.display_output()

    def srtf(self, processes):
        time = 0
        completed = 0
        n = len(processes)
        remaining_time = {p["pid"]: p["BT"] for p in processes}
        completion_time = {p["pid"]: 0 for p in processes}
        processes.sort(key=lambda x: x["AT"])

        while completed < n:
            eligible_processes = [p for p in processes if p["AT"] <= time and remaining_time[p["pid"]] > 0]
            if not eligible_processes:
                time += 1
                continue

            current = min(eligible_processes, key=lambda x: remaining_time[x["pid"]])
            pid = current["pid"]
            remaining_time[pid] -= 1
            time += 1

            if remaining_time[pid] == 0:
                completed += 1
                completion_time[pid] = time
                current["CT"] = completion_time[pid]
                current["TAT"] = current["CT"] - current["AT"]
                current["WT"] = current["TAT"] - current["BT"]

        return processes
    
    def fcfs(self, processes):
        processes.sort(key=lambda x: x["AT"])
        current_time = 0
        for process in processes:
            process["CT"] = max(current_time, process["AT"]) + process["BT"]
            process["TAT"] = process["CT"] - process["AT"]
            process["WT"] = process["TAT"] - process["BT"]
            current_time = process["CT"]
        return processes

    def sjf_non_preemptive(self, processes):
        processes.sort(key=lambda x: (x["AT"], x["BT"]))
        current_time = 0
        completed = []
        while processes:
            ready_queue = [p for p in processes if p["AT"] <= current_time]
            if not ready_queue:
                current_time = processes[0]["AT"]
                continue
            ready_queue.sort(key=lambda x: x["BT"])
            process = ready_queue.pop(0)
            processes.remove(process)

            process["CT"] = current_time + process["BT"]
            process["TAT"] = process["CT"] - process["AT"]
            process["WT"] = process["TAT"] - process["BT"]
            current_time = process["CT"]
            completed.append(process)
        return completed

    def priority_non_preemptive(self, processes):
        processes.sort(key=lambda x: (x["AT"], x["Priority"]))
        current_time = 0
        completed = []
        while processes:
            ready_queue = [p for p in processes if p["AT"] <= current_time]
            if not ready_queue:
                current_time = processes[0]["AT"]
                continue
            ready_queue.sort(key=lambda x: x["Priority"])
            process = ready_queue.pop(0)
            processes.remove(process)

            process["CT"] = current_time + process["BT"]
            process["TAT"] = process["CT"] - process["AT"]
            process["WT"] = process["TAT"] - process["BT"]
            current_time = process["CT"]
            completed.append(process)
        return completed

    def priority_preemptive(self, processes):
        processes.sort(key=lambda x: (x["AT"], x["Priority"]))
        current_time = 0
        completed = []
        ready_queue = []
        while processes or ready_queue:
            ready_queue.extend([p for p in processes if p["AT"] <= current_time])
            processes = [p for p in processes if p not in ready_queue]

            if not ready_queue:
                current_time += 1
                continue

            ready_queue.sort(key=lambda x: x["Priority"])
            process = ready_queue.pop(0)

            if "remaining_BT" not in process:
                process["remaining_BT"] = process["BT"]

            if process["remaining_BT"] > 1:
                process["remaining_BT"] -= 1
                ready_queue.append(process)
                current_time += 1
            else:
                current_time += process["remaining_BT"]
                process["CT"] = current_time
                process["TAT"] = process["CT"] - process["AT"]
                process["WT"] = process["TAT"] - process["BT"]
                completed.append(process)

        return completed

    def round_robin(self, processes, time_quantum):
        n = len(processes)
        completed = []
        queue = []
        current_time = 0
        remaining_bt = {process["pid"]: process["BT"] for process in processes}
        processes.sort(key=lambda x: x["AT"])
        queue.append(processes[0])
        processes.remove(processes[0])

        while queue or processes:
            if not queue:  
                current_time = processes[0]["AT"]
                queue.append(processes[0])
                processes.remove(processes[0])
        
        
            current_process = queue.pop(0)
            pid = current_process["pid"]
            execute_time = min(remaining_bt[pid], time_quantum)
            remaining_bt[pid] -= execute_time
            current_time += execute_time
            arrived_processes = [p for p in processes if p["AT"] <= current_time]
            queue.extend(arrived_processes)
            processes = [p for p in processes if p not in arrived_processes]

    
            if remaining_bt[pid] > 0:
                queue.append(current_process)
            else:
                current_process["CT"] = current_time
                current_process["TAT"] = current_process["CT"] - current_process["AT"]
                current_process["WT"] = current_process["TAT"] - current_process["BT"]
                completed.append(current_process)

        return completed


    def display_output(self):
        
        for row in self.output_table.get_children():
            self.output_table.delete(row)
        total_tat = 0
        total_wt = 0

        for process in self.process_data:
            self.output_table.insert("", "end", values=(
                process["pid"],
                process["AT"],
                process["BT"],
                process["CT"],
                process["TAT"],
                process["WT"]
            ))
            total_tat += process["TAT"]
            total_wt += process["WT"]

        num_processes = len(self.process_data)
        avg_tat = total_tat / num_processes if num_processes > 0 else 0
        avg_wt = total_wt / num_processes if num_processes > 0 else 0

        self.avg_tat_label.config(text=f"Average TAT: {avg_tat:.2f}")
        self.avg_wt_label.config(text=f"Average WT: {avg_wt:.2f}")


    def clear(self):
        for widget in self.process_entries:
            widget[0].destroy()  
            widget[1].destroy()  
            widget[2].destroy() 
    
  
        self.num_processes_entry.delete(0, tk.END)
        self.time_quantum_entry.delete(0, tk.END)
        self.algorithm.set("FCFS")
    
        self.process_entries = []  
        self.output_table.delete(*self.output_table.get_children())
        self.avg_tat_label.config(text="Average TAT: ")
        self.avg_wt_label.config(text="Average WT: ")

if __name__ == "__main__":
    root = tk.Tk()
    app = CPUSchedulingAnalyzer(root)
    root.mainloop()