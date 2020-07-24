from utils import *
from utils2 import getWeight

def main():
  a, b = getData()
  p, w = minMatchBruteGreedy(a, b)
  print ('Match:', p)
  print ('Peso:', w)


def minMatchBruteGreedy(a, b):
  n_blocks, n_pos_blocks = getBlocks(a)
  m_blocks, m_pos_blocks = getBlocks(b)
  print(n_blocks)
  print(m_blocks)
  m = []
  maxLen = max(len(n_blocks), len(m_blocks))
  minLen = min(len(n_blocks), len(m_blocks)) - 1
  len_a_blocks = len(n_blocks) - 1
  len_b_blocks = len(m_blocks) - 1
  a_i = 0
  b_j = 0
  for i in range(maxLen):
    if(i >= minLen):
      if(minLen == len_a_blocks):
        #print("division")
        m.append((n_blocks[a_i], []))
        for it in range(i, len_b_blocks + 1):
          m[i][1].append(m_blocks[it])
        break
      else:
        #print("Agrupación")
        m.append(([], (m_blocks[b_j])))
        for it in range(i, len_a_blocks + 1):
          m[i][0].append(n_blocks[it])
        break
    else:
      m.append((n_blocks[a_i], m_blocks[b_j]))
    if a_i < len(n_blocks) - 1:
      a_i += 1
    if b_j < len(m_blocks) - 1:
      b_j += 1
  return m, getWeight(m)


if __name__ == "__main__":
    main()
