def typedproperty(name, typ):
  private_name = '_' + name

  def getter(self):
    return getattr(self, private_name)

  def setter(self, value):
    if not isinstance(value, typ):
      raise TypeError(f'Expected {typ} got {value!r}')
    setattr(self, private_name, value)

  return property(getter, setter)

class Stock:
  __slots__ = ('_name', '_shares', '_price') # define allowed attributes
  name = typedproperty('name', str)
  shares = typedproperty('shares', int)
  price = typedproperty('price', float)

  def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

  def __repr__(self):
    # Note: The !r format code produces the repr() string
    # In Python format (f-string) strings, what does !r mean? - https://bit.ly/44q2oov
    return f'{type(self).__name__}({self.name!r}, {self.shares!r}, {self.price!r})'

  def __eq__(self, other):
    return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
            (other.name, other.shares, other.price))

  def __iter__(self):
    for i in [ self.name , self.shares , self.price ]:
      yield i


s = Stock('GOOG',100,490.10)
print(s.name) # 'GOOG'
print(s.shares)
print(s.price)
print()

# assigment test
s.shares = 50     # OK
# s.shares = '50'
# s.shares = 12.3
s.price = 123.45    # OK
# s.price = '123.45'
# s.price = 10
# s.notExist = 42

# iter
for val in s:
  print(val)

print(list(s))
print(tuple(s))
name, shares, price = s
print('name, shares, price ',name, shares, price )
