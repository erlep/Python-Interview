#!/usr/bin/env python

#  ===============================================
#   Python template file - Shebang Notation
#  ===============================================

# Shebang Notation: Python Scripts on Windows and Linux? - https://bit.ly/41UPRb8

#  ===============================================
#!/custom/tools/wrappers/lang/python
#!/custom/tools/lang/release7/python3.10.6/bin/python
#!/custom/tools/lang/release7/python3.9.0/bin/python
#!/custom/tools/lang/release7/python3.6.5/bin/python
#!/custom/tools/lang/release7/python3.7.9/bin/python
#!/custom/tools/lang/release7/python3.9.0/bin/python
#!/custom/tools/lang/release7/python3.10.0/bin/python
#!/custom/tools/lang/release7/python3.10.6/bin/python
#!/custom/tools/lang/release6/anaconda-3.5.1.0/bin/python
# -*- coding: utf-8 -*-

# Information about python interpreter
import sys
import os

# To check your Python verson inside a script use:
print('Python version:\n', sys.version)

# Find full path of the Python interpreter? - https://bit.ly/3Tu9OVx
print('Python interpreter full path:\n', sys.executable)

# Get Current Directory  - https://bit.ly/3RQYLEE
print('Current Directory:\n', os.getcwd())

# Command line
print("Cmd line:")
# argumenty
for args in sys.argv:
  print(args, end=" ")

print("\nKonec")

# Output:
# Python 3.6.4 :: Anaconda, Inc.

# export PATH="/custom/tools/lang/release7/python3.9.0/bin/:$PATH"
# export PATH="/custom/tools/lang/release7/python3.6.5/bin/:$PATH"
