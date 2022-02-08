# vyhod nejmensi integer (pro stejne cisla to prvni)

# The museum of incredible dull things - https://bit.ly/34GCnYi

# remove_smallest([1,2,3,4,5]) => [2,3,4,5]
# remove_smallest([5,3,2,1,4]) => [5,3,2,4]
# remove_smallest([2,2,1,2,1]) => [2,2,2,1]
# remove_smallest([2]) => []
# remove_smallest([6, 6, 6, 6]) => [6, 6, 6]
# remove_smallest([6, 6, 6, 2]) => [6, 6, 6]
# remove_smallest([6, 6, 5, 6]) => [6, 5, 6]

def remove_smallest(arr):
  # prvni hodnota
  minValue = arr[0]
  # najdi min hodnotu
  for num in arr:
    if num < minValue:
      minValue = num
  # shallow copy
  newArr = arr[:]
  # smaz min hodnotu
  newArr.remove(minValue)
  print(arr, ' => ', newArr)
  return newArr

a = remove_smallest([1, 2, 3, 4, 5])
a = remove_smallest([1, 2, 3, 4, 5, 1])
a = remove_smallest([5, 3, 2, 1, 4])
a = remove_smallest([2, 2, 1, 2, 1])
a = remove_smallest([2])
a = remove_smallest([6, 6, 6, 6])
a = remove_smallest([6, 6, 6, 2])
a = remove_smallest([6, 6, 5, 6])
