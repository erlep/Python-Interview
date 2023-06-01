#!/usr/bin/env python

a = 1
b = a
print ('a',a)
print ('b',b)
a=2
print ('a',a)
print ('b',b)

la = [1,2,3]
lb = la  # crate new link to list
# lb = la[:] # shallow copy
print ('la',la)
print ('lb',lb)
la.append(4)
print ('la',la)
print ('lb',lb)
