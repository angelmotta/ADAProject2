from utils import *


def main():
  a, b = getData()
  p, w = minMatchBruteGreedy(a, b)
  print ('Pares:', p)
  print ('Peso:', w)


def minMatchBruteGreedy(a, b):
  n_blocks = getBlocks(a)
  m_blocks = getBlocks(b)
  m = []
  maxLen = max(len(n_blocks), len(m_blocks))
  a_i = 0
  b_j = 0
  for i in range(maxLen):
    m.append((a_i, b_j))
    if a_i < len(n_blocks) - 1:
      a_i += 1
    if b_j < len(m_blocks) - 1:
      b_j += 1
  return m, calcWeight(n_blocks, m_blocks, m)


if __name__ == "__main__":
    main()
