import sys

print(sys.argv)
if len(sys.argv) < 3:
    raise IOError("You must provide username and password")