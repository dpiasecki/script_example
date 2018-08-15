import sys

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

print(first + second)