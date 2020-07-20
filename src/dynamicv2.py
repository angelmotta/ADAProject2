import math
from utils import *
from utils2 import *


def main():
    a, b = getData()
    minMatchDynamic(a, b)
    #p, w = minMatchDynamic(a, b)
    #print ('Min Match:', p)
    #print ('Weight:', w)
    #print(reg)


reg = {}


def minMatchDynamic(a, b):
    a_blocks = getBlocks(a)
    b_blocks = getBlocks(b)
    minMatchDynamicUtil(a_blocks, b_blocks)
    #minMatch = minMatchDynamicUtil(a_blocks, b_blocks)
    #weight = getWeight(minMatch)
    #return minMatch, weight


def minMatchDynamicUtil(a_blocks, b_blocks):
    lenA = len(a_blocks)
    lenB = len(b_blocks)
    minLen = min(lenA, lenB)
    dif = minLen - 1
    idxA = (lenA - dif) - 1
    idxB = (lenB - dif) - 1
    listMatches = []
    match = []
    for it in range(max(idxA + 1, idxB + 1)):
        print(it)


    '''
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
        if reg.get(i):
            if reg[i].get(j):
                return reg[i][j].copy()
        listMatches = []
        match = []
        match = minMatchUtil(a_blocks[:i], b_blocks[:j])
        match.append((a_blocks[i], b_blocks[j]))
        listMatches.append(match)
        for it in range(1, i):
            matches = minMatchUtil(a_blocks[:it], b_blocks[:j])
            match = ([], b_blocks[j])
            for idx_block_a in range(it, i + 1):
                match[0].append(a_blocks[idx_block_a])
            matches.append(match)
            listMatches.append(matches)
        for it in range(1, j):
            matches = minMatchUtil(a_blocks[:i], b_blocks[:it])
            match = (a_blocks[i], [])
            for idx_block_b in range(it, j + 1):
                match[1].append(b_blocks[idx_block_b])
            matches.append(match)
            listMatches.append(matches)
        minMatchRes = getMinWeigthMatch(listMatches)
        if reg.get(i):
            reg[i][j] = minMatchRes
        else:
            reg[i] = {}
            reg[i][j] = minMatchRes
        return reg[i][j].copy()
    '''


if __name__ == "__main__":
    main()
