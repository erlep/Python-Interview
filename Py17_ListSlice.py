# -*- coding: utf-8 -*-

print('Sequence Containers Indexing - lst[start slice:end slice:step]')
lst = [10, 20, 30, 40, 50]
print('lst:', lst)
print('lst[:-1]', lst[:-1])
print('lst[::-1]', lst[::-1])
print('lst[1:3]', lst[1:3])
print('lst[:3]', lst[:3])
print('lst[1:-1]', lst[1:-1])
print('lst[::-2]', lst[::-2])
print('lst[-3:-1]', lst[-3:-1])
print('lst[3:]', lst[3:])
print('lst[::2]', lst[::2])
# shallow copy of sequence
print('lst[:]', lst[:])
# zrusi 3
print('lst:', lst)
lst[1:4] = [15, 25]
print('lst[1:4] = [15, 25] \nlst:', lst)

lst = [10, 20, 30, 40, 50]
lst2 = lst[:]
lst[1:4] = [15, 25]

print()
print('lst:', lst)
print('lst2:', lst2)

# kopie 5x za sebe
lst5 = lst*5
print('lst5:', lst5)

# spojeni za sebe
lstA = lst + lst2
print('lstA:', lstA)
# Pozice
print('lstA.index(40):', lstA.index(40))
# Vyskyt
print('lstA.count(50):', lstA.count(50))



# Prohozeni promenych
a = 1
b = 2
print('a:', a)
print('b:', b)
a, b = b, a
print('a:', a)
print('b:', b)



# unpacking of sequence in item and list
seq = [11, 12, 13, 14]
a, *b = seq
print('a, *b = seq:', seq)
print('a:', a)
print('b:', b)

*a, b = seq
print('*a, b = seq:', seq)
print('a:', a)
print('b:', b)

