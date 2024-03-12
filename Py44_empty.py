#!/usr/bin/env python

# 5 Must-Know HIDDEN Features - https://youtu.be/nrN3Gq1A92Y?si=tCkknbGatUT5w_M4

# _ - Anonymous Variable
list_of_pairs = [["A", "B"], ["C", "D"], ["E", "F"]]
print(f'{list_of_pairs=}')
second_elements = [b for _, b in list_of_pairs]
print(f'{second_elements=}')
