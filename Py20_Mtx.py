# Matice 1. radek a 1. sloupec

M = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]

print('Matice')
print(M, type(M))
print()

print('1. radek')
print(M[0], type(M[0]))
print()

# How do you extract a column from a multi-dimensional array? - https://bit.ly/3ELUIQm
print('1. sloupec')
#  Radky za sloupce
S = list(zip(*M))
# print(S, type(S))
print(S[0], type(S[0]))
print()
