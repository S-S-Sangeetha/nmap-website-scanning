# Automated Nmap Scanner

## The Problem
Running Nmap scans manually is slow and the output needs to be manually copied and saved. Security analysts need a fast way to scan targets and log the results for reporting.

## The Solution
This is a Python script that automates Nmap scans (`-sV -F`), prints the results directly to the terminal, and automatically saves the output to a `.txt` file for future reference.

## How It Works
- Uses Python's `subprocess` module to execute Nmap securely.
- Includes error handling (checks if Nmap is installed).
- Parses the target IP via command-line arguments.

## How to Run It
1. Ensure you have Python 3 and Nmap installed.
2. Clone this repo.
3. Run the script:
   ```bash
   python scanner.py 127.0.0.1

## What I Learned
- How to use Python's `subprocess` module to run system commands securely.
- How to handle file input/output (I/O) in Python.
- How to use command-line arguments (`sys.argv`) to make scripts reusable.

## Screenshot
<img width="1192" height="666" alt="image" src="https://github.com/user-attachments/assets/1f9f5d0c-0b66-48e8-86a6-d2732cb30fe0" />
