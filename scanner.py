import subprocess
import sys

def run_scan(target_ip):
    print(f"[*] Starting scan on {target_ip}...")
    try:
        # -sV detects service versions, -F scans top 100 ports for speed
        command = ["nmap", "-sV", "-F", target_ip]
        
        # Run the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        print("\n[+] Scan Results:")
        print(result.stdout)
        
        # Save the output to a text file
        filename = f"scan_results_{target_ip.replace('.', '_')}.txt"
        with open(filename, "w") as file:
            file.write(result.stdout)
        print(f"[+] Results saved to {filename}")

    except subprocess.CalledProcessError as e:
        print(f"[!] Error running Nmap: {e}")
    except FileNotFoundError:
        print("[!] Nmap is not installed. Please install Nmap first.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 scanner.py <target_ip>")
        sys.exit(1)
    
    target = sys.argv[1]
    run_scan(target)
