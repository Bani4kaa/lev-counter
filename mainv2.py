import subprocess

def execute_detect_script():
    command = ['python', 'detect.py', '--source', '2', '--device', '0', '--weights', 'best.pt']
    
    try:
        # Execute the command
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print("Error executing command:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    execute_detect_script()