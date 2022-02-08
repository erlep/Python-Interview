# Complete the solution so that it reverses the string passed into it. - https://bit.ly/34E9zj9
# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

def revers(retezec):
  mylist = list(retezec)
  mylist.reverse()
  newString = ''.join(mylist)
  print(retezec, ' => ', newString)
  return newString

a = revers('world')  # =>  'dlrow'
a = revers('word')  # =>  'dlrow'
