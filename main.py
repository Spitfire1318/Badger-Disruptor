import os
import time
import webbrowser
import argparse
import wmi

ti = 0

pr_name = 'Google_Chrome'
f = wmi.WMI()
for process in f.Win32_Process():
     
    # Checking whether the process
    # name matches our specified name
    if process.name == pr_name:
 
        # If the name matches,
        # terminate the process   
        process.Terminate()
     
        # This increment would acknowledge
        # about the termination of the
        # Processes, and would serve as
        # a counter of the number of processes
        # terminated under the same name
        ti += 1
        
if ti == 0:
 
    # An output to inform the
    # user about the error
    print("Process not found!!!")
