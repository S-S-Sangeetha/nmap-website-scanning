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
   python3 scanner.py 192.168.1.1

#### Step 3: Prove It Works
1. Run your new Python script in your terminal.
2. Take a **screenshot** of the terminal showing the script running and the output.
3. Put that screenshot in the README file (drag and drop it into GitHub when editing).

---

### Why This Works (The Interview Magic)

Do you see what we just did? 

Before, if an interviewer asked you about this repo, you would say: *"I ran nmap -sV on an IP."* (They would move to the next candidate).

Now, when they ask, you say: *"I wanted to practice Python for security, so I built an automation script. I used the `subprocess` module to run Nmap, and I added error handling in case Nmap isn't installed. It saves the output to a text file so an analyst doesn't have to copy-paste it manually."* 

That is a **Junior Security Automation Engineer** answer.

### Do this for one more repo
Do the exact same thing for `nikto-vulnerability-scan`. Change the command in the Python script to run Nikto instead of Nmap. 

Now, your GitHub has **two real Python automation projects**. You don't need 6 messy repos. Two polished, working Python scripts with great READMEs will get you hired faster than 20 copied assignments. 

Go spend 1 hour on this right now. Then update your resume to include the "Projects" section I gave you in the last message. You are incredibly close to being ready.
