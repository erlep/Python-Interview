# lambda - is anonymous function

def sum_map(func, nums):
  total = 0.0
  for num in nums:
    total += func(num)
  return total

nums = [1, 2, 3, 4]
r = sum_map(lambda x: x ** 2, nums)
print(r)
