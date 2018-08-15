import sys
import subprocess

try:
  first = int(sys.argv[1])
except (IndexError, NameError, ValueError):
  print("first input not defined or not a number")
  sys.exit(1)

try:
  second = int(sys.argv[2])
except (IndexError, NameError, ValueError):
  print("second input not defined or not a number")
  sys.exit(1)

command="python add.py "+str(first)+" "+str(second)

total=subprocess.check_output(command, shell=True)

#print(total)

file = open("total.txt", "w")
file.write(total)
file.close()