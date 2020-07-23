def getData():
  a = []
  b = []

  print('Values of vector A')
  m = input()
  for i in m.split():
    a.append(int(i))

  print('Values of vector B')
  m = input()
  for i in m.split():
      b.append(int(i))
  
  return a, b


## Brute get Blocks corregir
def getBlocks(arr):
  arr_blocks = []
  pos_blocks = []
  seg = 0
  prev = -1
  idx = 0
  xi = 0
  xf = 0
  isFirstTime = True
  for num in arr:
    if num == 1:
      if isFirstTime:
        xi = idx
        isFirstTime = False
      seg += 1
    elif num == 0 and prev == 1:
      xf = idx
      isFirstTime = True
      arr_blocks.append(seg)
      seg = 0
      pos_blocks.append((xi, xf - 1))
    prev = num
    idx += 1
  if seg > 0:
    arr_blocks.append(seg)
    pos_blocks.append((xi, idx - 1))
  print("Positions blocks")
  print(pos_blocks)
  return arr_blocks, pos_blocks


def simplePair(a, b):
  m = []
  for i in range(a):
    for j in range(b):
      m.append((i,j))
  return m

def staticPair(a, b):
  m = []
  for i in a:
    for j in b:
      m.append((i, j))
  return m

def calcWeight(a, b, pairs):
  last_a = pairs[0][0] 
  last_b = pairs[0][1]

  num = a[last_a]
  dem = b[last_b]

  result = 0

  for p in pairs[1:]:
    c_a = last_a == p[0]
    c_b = last_b == p[1]

    if c_a:
      dem += b[p[1]]
    elif c_b:
      num += a[p[0]]
    else:
      result += num / dem
      num = a[p[0]]
      dem = b[p[1]]
    last_b = p[1]
    last_a = p[0]
  
  result += num / dem
  
  return result