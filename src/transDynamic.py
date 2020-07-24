import math
from utils import *
from utils2 import *


def main():
    A = []
    A.append([1, 1, 0, 1, 1, 1])
    A.append([0, 1, 1, 1, 1, 1])
    A.append([1, 1, 0, 0, 1, 1])
    B = []
    B.append([0, 0, 1, 1, 0, 1])
    B.append([0, 0, 1, 1, 1, 1])
    B.append([1, 0, 1, 0, 1, 1])
    M, W = transDynamic(A, B)
    print('Transformacion:', M)
    print('Peso:', W)


def minMatchDynamic(a, b):
    a_blocks, a_pos_blocks = getBlocks(a)
    b_blocks, b_pos_blocks = getBlocks(b)

    n = len(a_blocks)
    m = len(b_blocks)

    reg = [[math.inf for x in range(m)] for y in range(n)]

    p = {}

    for i, ax in enumerate(a_blocks):
        for j, bx in enumerate(b_blocks):
            if i == 0:
                if j == 0:
                    reg[i][j] = ax / bx
                else:
                    reg[i][j] = cost([0], range(j + 1), a_blocks, b_blocks)
                continue
            if j == 0:
                reg[i][j] = cost(range(i + 1), [0], a_blocks, b_blocks)
                continue

            mn = math.inf

            for k in range(i):
                t = reg[k][j - 1]
                c = cost(range(k + 1, i + 1), [j], a_blocks, b_blocks)
                if t + c < mn:
                    mn = t + c
                    p[(i, j)] = (k, j - 1)

            for k in range(j):
                t = reg[i - 1][k]
                c = cost([i], range(k + 1, j + 1), a_blocks, b_blocks)
                if t + c < mn:
                    mn = t + c
                    p[(i, j)] = (i - 1, k)

            reg[i][j] = mn

    # Construccion de la solucion

    c = (n - 1, m - 1)
    pairs = []
    while c[0] != 0 and c[1] != 0:
        d = p[c]
        pairs.append(constuct_pair(d, c, a_blocks, b_blocks))
        c = d
    pairs.append(constuct_pair((-1, -1), c, a_blocks, b_blocks))
    pairs.reverse()

    return pairs, reg[n - 1][m - 1]


def constuct_pair(a, b, a_blocks, b_blocks):
    dx = abs(a[0] - b[0])
    t = []
    if dx == 1:
        for i in range(a[1] + 1, b[1] + 1):
            t.append(b_blocks[i])
        return (a_blocks[b[0]], t)
    else:
        for i in range(a[0] + 1, b[0] + 1):
            t.append(a_blocks[i])
    return (t, b_blocks[b[1]])


def cost(a, b, ab, bb):
    xa = 0
    for ai in a:
        xa += ab[ai]
    xb = 0
    for bi in b:
        xb += bb[bi]
    return xa / xb


def transDynamic(A, B):
    M = []
    W = 0
    for idx in range(len(A)):
        rowA = A[idx]
        rowB = B[idx]
        minMatch, w = minMatchDynamic(rowA, rowB)
        M.append(minMatch)
        W += w
    return M, W


if __name__ == "__main__":
    main()
