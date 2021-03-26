# -*- coding: utf-8 -*-
# Preparing for Programming interview with Python - https://is.gd/RfZHKP

# Log-search Techniques - hledani pulenim intervalu
def LogSearch():
  arr, target = [1, 2, 3, 4, 5], 3
  start, end = 0, len(arr)-1
  while start <= end:
    mid = int((start+end)/2)
    if arr[mid] == target:
      return 'search for: ' + str(target) +'  position: ['+ str(mid) + '] -> value: ' + str(arr[mid])  # The value is found
    else:
      if arr[mid] < target:
        start = mid+1
      else:
        end = mid-1
  return -1  # The value is not found
st = LogSearch()
print('st: ', st)

"""
Priklady jak List
#List traversal
range(start, stop, hop)
range(n) # [0,1,...,n-1]
range(1,n) # [1,...,n-1]
range(1,n,2) # [1,3,5,...,n-1] if n is even, or [1,3,5,...,n-2] if n is odd
range(n,-1,-1) # [n,n-1,n-2,...,0]
range(len(arr)) # Provides indices of an array arr
range(len(arr)-1,-1,-1) # Provides indices of arr backwards

# List slicing
arr[w:s] # Wait w elements, start copy (:), stop before reaching index s
arr = [1,2,3,4]
arr[1:] = [2,3,4]
arr[:2] = [1,2]

#List manipulation
arr = [1,2,3]
[str(x) for x in arr] # Output: ['1','2','3']
map(lambda x: str(x), arr) # Output: ['1','2','3']
[str(x) for x in arr if x%2] # Output: ['1','3']

# List as queue
arr = [1,2,3]
arr.append(x) # queue.push(x)
arr.pop(0) #queue.pop()
arr[0] #queue.peek()

# List as stack
arr = [1,2,3]
arr.append(x) #stack.push(x)
arr.pop() # stack.pop()
arr[-1] # stack.peek()
"""

# loops
counter = 0
while counter <= 5:
  print('counter: ', counter)
  counter += 1
else:
  print("loop exited normally")
# Output: 0 1 2 3 4 5 loop exited normally

for i in range(5):
  print('i: ', i)
  if i > 3:
    break
else:
  print("loop exited normally")
# Output: 0 1 2 3 4
