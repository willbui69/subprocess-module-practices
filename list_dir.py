### A simple program to list all files in a folder

# Import subprocess module so we can use os commands
import subprocess

# To save output of a process we set capture_output = True
# To store the output as a string, we set text = True
list_of_files = subprocess.run(['ls', '-la'], capture_output = True, text = True)

# To access the output of a process, we use stdout
print(list_of_files.stdout)