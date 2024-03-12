# Class Attributes
class Date:
  datefmt = '{year}-{month}-{day}'  # there is no 'self.'  ! - Class Attributes
  def __init__(self, year, month, day):
    self.year = year
    self.month = month
    self.day = day
  def __str__(self):
    return self.datefmt.format(year=self.year,
                               month=self.month,
                               day=self.day)
class USDate(Date):
  datefmt = '{month}/{day}/{year}'

d_mil = Date('2023', '06', '28')
print("d_mil", d_mil)
d_usa = USDate('2023', '06', '28')
print("d_usa", d_usa)
print()

# Class Methods - @classmethod & cls - pracuje primo se tridou NE s instanci tridy
# ● Class methods can be called from the class
# ● They take the class (cls) instead of self as the first
class DataConnection:
  active = True
  @classmethod
  def toggle(cls):
    cls.active = not cls.active
print("DataConnection.active:", DataConnection.active)
DataConnection.toggle()
print("DataConnection.toggle()")
print("DataConnection.active:", DataConnection.active)
