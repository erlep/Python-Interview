# Python Decorators: The Secret to Supercharging Your Code https://youtu.be/UuHuNDdOPz0?si=BFbdBlQ8cmHGIBIw
# Python Decorators, A Beginners Guide (With Code Examples) - https://k0nze.dev/posts/python-decorators

def count_instances(msg="new instance of"):
  def decorator(cls):
    class CountInstances(cls):
      count = 0

      def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.msg = msg
        CountInstances.count += 1

      def print_msg(self):
        print(f"{self.msg}")

    return CountInstances
  return decorator


@count_instances("Hello")
class Foo:
  def __init__(self, cislo):
    self.cislo = cislo

if __name__ == "__main__":
  foo0 = Foo(42)
  foo0.print_msg()
  print(f'CountInstances: {foo0.count=}')
  print(f'{foo0.cislo=}')

  foo1 = Foo(23)
  foo1.print_msg()
  print(f'CountInstances: {foo1.count=}')
  print(f'{foo1.cislo=}')
