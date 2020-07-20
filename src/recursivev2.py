import math
from utils import *
from utils2 import *

def main():
  a, b = getData()
  p, w = minMatch(a, b)
  print ('Min Match:', p)
  print ('Weight:', w)


def minMatch(a, b):
    a_blocks = getBlocks(a)
    b_blocks = getBlocks(b)
    minMatch = minMatchUtil(a_blocks, b_blocks)
    weight = getWeight(minMatch)
    return minMatch, weight


def minMatchUtil(a_blocks, b_blocks):
    i = len(a_blocks) - 1
    j = len(b_blocks) - 1
    if i == 0 and j == 0:
        return [(a_blocks[i], b_blocks[j])]
    elif i == 0 or j == 0:
        if i == 0:
            match = (a_blocks[i], [])
            for it in range(j + 1):
                match[1].append(b_blocks[it])
            return [match]
        else:
            match = ([], b_blocks[j])
            for it in range(i + 1):
                match[0].append(a_blocks[it])
            return [match]
    else:
        listMatches = []
        match = minMatchUtil(a_blocks[:i], b_blocks[:j])
        match.append((a_blocks[i], b_blocks[j]))
        listMatches.append(match)
        for it in range(1, i):
            matches = minMatchUtil(a_blocks[:it], b_blocks[:j])
            match = ([], b_blocks[j])
            for elm in range(it, i + 1):
                match[0].append(a_blocks[elm])
            matches.append(match)
            listMatches.append(matches)
        for it in range(1, j):
            matches = minMatchUtil(a_blocks[:i], b_blocks[:it])
            match = (a_blocks[i], [])
            for idx_block_b in range(it, j + 1):
                match[1].append(b_blocks[idx_block_b])
            matches.append(match)
            listMatches.append(matches)
        return getMinWeigthMatch(listMatches)


if __name__ == "__main__":
    main()
