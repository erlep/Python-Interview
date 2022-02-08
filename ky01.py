# The museum of incredible dull things - https://bit.ly/34GCnYi

# remove_smallest([1,2,3,4,5]) = [2,3,4,5]
# remove_smallest([5,3,2,1,4]) = [5,3,2,4]
# remove_smallest([2,2,1,2,1]) = [2,2,2,1]


def remove_smallest(arr):
  index = 0
  minValue = 1000000
  for i, num in enumerate(arr):
    if num < minValue:
      index = i
      minValue = num

  i = 0
  for num in arr:
    if i <> index:
      newArr[i] = num
      i += 1

  return newArr


remove_smallest([1, 2, 3, 4, 5]) = [2, 3, 4, 5]
