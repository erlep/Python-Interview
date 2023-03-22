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

# To check your Python verson inside a script use:
import sys
print(sys.version)
print('')


print('Cmd line:')
# argumenty
for args in sys.argv:
  print(args, end=' ')

print('konec')


# Output:
# Python 3.6.4 :: Anaconda, Inc.

# export PATH="/custom/tools/lang/release7/python3.9.0/bin/:$PATH"
# export PATH="/custom/tools/lang/release7/python3.6.5/bin/:$PATH"
