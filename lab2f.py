#!/usr/bin/env python3
#Author; Sabin bhujel
#Author ID: 180147217
#Date Created :2024/05/24
import sys 
if len(sys.argv) !=2:
    print(f"Usage : {sys.argv[0]} <countdown_start>")
    sys.exit(1)
try:
    timer = int(sys.argv[1])
except ValueError:
        print(f"Error: {sys.argv[1]} is not a valid integer.")
        sys.exit(1)

while timer > 0:
    print(timer)
    timer -= 1
print("blast off!")

