import subprocess

def run_bash_command(command):    
    try:
        # Execute the command and capture the output
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        # Print the standard output from the command
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        # Print the error if the command fails
        print(f"Error: {e.stderr}")
def run_commands_from_file(file_path):
    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            commands = file.read()

        # Execute the commands
        result = subprocess.run(commands, shell=True, check=True, text=True, capture_output=True)
        
        # Print the standard output from the command
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        # Print the error if the command fails
        print(f"Error: {e.stderr}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")