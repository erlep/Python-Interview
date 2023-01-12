#!/usr/bin/env python3
# https://www.w3schools.com/python/python_file_open.asp
# https://www.geeksforgeeks.org/how-to-read-from-a-file-in-python/


# Program to show various ways to read data from a file.

L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
FlNm = 'Text.Txt'

# Creating a file
with open(FlNm, "w") as file1:
  # Writing data to a file
  file1.write("Hello \n")
  file1.writelines(L)
  file1.close()  # to change file access modes


# How do I check whether a file exists without exceptions? https://bit.ly/3BfE77g
if not (os.path.isfile(FlNm)):
  print("File does not exist!")
  exit(1)

with open(FlNm, "r+") as file1:
  # Reading form a file
  print(file1.read())
