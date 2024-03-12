class Dog:
  def noise(self):
    return 'Woof'
class Bike:
  def noise(self):
    return 'Ding!'
class Loud:
  def noise(self):
    return super().noise().upper()
class LoudDog(Loud, Dog,):
  pass
class LoudBike(Loud, Bike):
  pass

print('  Noises:')
d = Dog()
print(d.noise())
b = Bike()
print(b.noise())

print('  Load noises:')
ld = LoudDog()
print(ld.noise())
lb = LoudBike()
print(lb.noise())
