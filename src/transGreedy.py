from utils import *
from utils2 import *
from greedy import minMatchBruteGreedy

def main():
    A = []
    A.append([1, 1, 0, 1, 1, 1])
    A.append([0, 1, 1, 1, 1, 1])
    A.append([1, 1, 0, 0, 1, 1])
    B = []
    B.append([0, 0, 1, 1, 0, 1])
    B.append([0, 0, 1, 1, 1, 1])
    B.append([1, 0, 1, 0, 1, 1])
    M, W = transGreedy(A, B)
    print('Transformacion:', M)
    print('Peso:', W)


def transGreedy(A, B):
    M = []
    W = 0
    for idx in range(len(A)):
        rowA = A[idx]
        rowB = B[idx]
        match, w = minMatchBruteGreedy(rowA, rowB)
        M.append(match)
        W += w
    return M, W


if __name__ == "__main__":
    main()
