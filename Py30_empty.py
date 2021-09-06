#!/usr/bin/env python3

a = 1
print(type(a))

a = 1.123456789101223
print(type(a))

a = 0x123
print(type(a))


a = '1.1'
print(type(a))

m = [1, 2.2, 3, 4, 5, 6, 7, 8.81234567890001]

# vsechny stejny typ
print(all((type(t) == int) or (type(t) == float) for t in m))

a = [1, 2, 3]
print(a)

b = [a]
print(b)
