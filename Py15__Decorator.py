# Decorators
# Try THIS Simple Python Decorator (It's Super Useful) - https://youtu.be/4WQba4KwmRs
# Decorators in Python - https://www.geeksforgeeks.org/decorators-in-python/

def scitaci_zaznam(funkce):
  'pocita volani funkce'
  class Wrapper:
    'objekt pocitani volani'
    def __init__(self):
      'konstruktor'
      self._count = 0
      self._jmeno = ''

    def __call__(self, *args, **kwargs):
      'proste __call__'
      # print('__call__', func.__name__)
      self._jmeno = funkce.__name__
      wrapper.count += 1
      return funkce(*args, **kwargs)

    @property
    def count(self):
      'get property count'
      # print('get: self._count', self._count)
      return self._count

    @count.setter
    def count(self, value):
      'set property count'
      # print('set: self._count', self._count,'  value', value)
      self._count = value
      print(f'Pocet volani {self._jmeno} je {self.count}')
  # telo funkce
  wrapper = Wrapper()
  wrapper.__call__ = funkce
  return wrapper

@scitaci_zaznam
def FunkceABC():
  print("Ahoj světe!")

FunkceABC()
FunkceABC()
FunkceABC()
