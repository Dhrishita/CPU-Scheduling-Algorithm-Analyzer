# CPU Scheduling Algorithm Analyzer
A Python-based CPU Scheduling Algorithm Analyzer with a GUI using Tkinter. It simulates various CPU scheduling algorithms (FCFS, SJF, Round Robin, Priority, SRTF), calculates turnaround and waiting times, and provides detailed outputs for better understanding of scheduling behavior.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologiesused)
- [Installation](#installation)
- [Usage](#usage)
- [Working of the Application](#workingoftheapplication)
- [Error Handling](#errorhandling)
- [Contact](#contact)

## Introduction

Welcome to the **CPU Scheduling Algorithm Analyzer**! 🚀 This interactive Python application allows you to explore the fascinating world of CPU scheduling. With a user-friendly GUI built using Tkinter, you can simulate popular algorithms like FCFS, SJF, Round Robin, Priority, and SRTF. Dive into the code and experience firsthand how each algorithm optimizes CPU resource allocation, and see the impact on waiting and turnaround times. Whether you're a student learning about OS concepts or a developer curious about algorithm efficiency, this tool is designed to make CPU scheduling both fun and insightful. Check out the code and start experimenting!


## Features

- **Algorithm Selection** - Users can choose from multiple CPU scheduling algorithms, including:
   - FCFS (First-Come, First-Served)
   - SJF (Shortest Job First)
   - Priority Scheduling (Preemptive and Non-Preemptive)
   - Round Robin
   - SRTF (Shortest Remaining Time First)

- **Dynamic Process Input** - Users can input the number of processes and their corresponding arrival time, burst time, and priority for accurate simulation.

- **Time Quantum** - For Round Robin scheduling, users can specify the time quantum.

- **Output Display** - The output includes detailed tables showing:
  - Process ID
  - Arrival Time (AT)
  - Burst Time (BT)
  - Completion Time (CT)
  - Turnaround Time (TAT)
  - Waiting Time (WT)
  
- **Average Times** - The tool calculates and displays the average Turnaround Time (TAT) and Waiting Time (WT) for the processes.

## Technologies Used

- **Python** - The powerhouse behind the entire application, providing robust functionality and seamless performance.
- **Tkinter** - A simple yet powerful python library for crafting a sleek, intuitive GUI that makes interacting with algorithms a breeze.
- **ttk (Themed Tkinter)** - For more advanced and aesthetically pleasing widgets.
- **Pandas (optional for advanced data handling)** - If needed for handling large datasets or complex calculations.
  
## Installation

1. Clone this repository to your Raspberry Pi:
   
   ```bash
   git clone https://github.com/yourusername/CPU-Scheduling-Analyzer.git

2. Install Python (if not installed):
   - Download and install Python from python.org.
     
3. Install Required Libraries: Use pip to install Tkinter (usually pre-installed with Python) and any additional dependencies (like Pandas, if needed):
   
   ```bash
   pip install pandas
   
4. Run the Application: Navigate to the project directory and run the Python file:

   ```bash
   python3 main.py

## Usage

1. **Select Scheduling Algorithm** - Choose the CPU scheduling algorithm you wish to simulate (FCFS, SJF, Priority, Round Robin, SRTF).

2. **Enter Process Data** - Input the number of processes and their respective arrival time, burst time, and priority (if applicable). If using Round Robin, enter the time quantum as well.

3. **Run Simulation** - Click the Calculate button to simulate the chosen algorithm. The output will display the process table with computation results (CT, TAT, WT).

4. **Clear Data** - If you wish to reset the inputs and try with different values, click the Clear button.
  

## Working of the Application (Socket Programming)

1. **Input Validation** - The application validates user input for number of processes, arrival time, burst time, and priority. It ensures that all fields are filled with valid data before running the simulation.

2. **Scheduling Algorithms** - The app calculates the results based on the selected scheduling algorithm and updates the output table with the computed values for Completion Time, Turnaround Time, and Waiting Time.

3. **Time Calculation**
   - **For Non-preemptive algorithms** like FCFS, SJF, and Priority, the process runs to completion once started.
   - **For Preemptive algorithms** like Round Robin and SRTF, processes may be interrupted based on conditions like time quantum or remaining burst time.


## Error Handling

- **Invalid Input** - If the user enters non-integer values for time, burst time, or priority, the application will display an error message prompting the user to correct the input.

- **Empty Input** - If the process fields are empty, the application will notify the user to provide values for all processes.

- **Invalid Time Quantum** - For Round Robin scheduling, if the time quantum field is empty or contains invalid data, the application will display an error message.

## Contact
If you have any questions or suggestions, feel free to open an issue or contact:
Dhrishita Parve: dhrishitap18@gmail.com
