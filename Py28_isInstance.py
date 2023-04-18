#!python3
#!/usr/bin/env python3

# Check if a string is hexadecimal - https://bit.ly/3iAkyS6
# inp = '0xa'
aInp = [12, 0x10, '21', '0xa', -5, 'g', 3.14]
print(aInp)

# address & bit value in string, int or hex format
for inp in aInp:
  if isinstance(inp, int):
    # int
    # print('integer or hexadecimal')
    val = inp
  elif isinstance(inp, float):
    # string
    print('neni spravna hodnota')
    val = 0
  elif isinstance(inp, str):
    # string
    try:
      # string int
      val = int(inp)
    except ValueError:
      # string hex
      try:
        # string int
        val = int(inp, 16)
      except ValueError:
        print('neni spravna hodnota')
        val = 0

  print('inp', inp, '  val', val, type(val))
