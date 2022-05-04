### A program to check whether a list of programs are installed or not

import subprocess

# Import pyinputplus module for input validation
import pyinputplus as pyip

# Import re module for regular expressions
import re

# Ask the user to list the names of programs to check
programs = pyip.inputStr(prompt='Enter the program\'s name to check:').split()

# Program names include only words and digits
program_reg = re.compile(r'\w\d')

# Check every program name
for program in programs:
    if not re.match(program_reg, program):
        print(f"We can't check the program {program}")
        continue

    process = subprocess.run(['which', program], capture_output = True, text = True)
    if process.returncode == 0:
        print(f"The program {program} is installed")
        print(f"The location of the binary is: {process.stdout}")
    else:
        print(f"The program {program} is not installed")
        print(process.stderr)
