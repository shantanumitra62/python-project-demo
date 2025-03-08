import subprocess
import os

curr_wrkng_dir=os.getcwd()
print(f"Current workDir is {curr_wrkng_dir}")

# Using OS module to list files in CUR_WRKNG_DIR

files=os.listdir(curr_wrkng_dir)

if os.name=="posix":
    command=['ls', '-lrt']
elif os.name=='nt':
    command=['dir']
    command=['ipconfig']

#Now run the command
try:
    result=subprocess.run(command, check=True, text=True, capture_output=True, shell=True)
    print("command output")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print("Exception caught",e)
finally:
    print("Ending the code block")