#!/usr/bin/python3 

import subprocess

P1=subprocess.call(["ping","-c","5","google.com"]) 
print(P1)
