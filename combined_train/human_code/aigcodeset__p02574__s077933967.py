import numpy as np
from numba import njit

def f1():
    v1 = int(input())
    v2 = np.array(list(map(int, input().split())))

    def gdc(a1, a2):
        v1 = max(a1, a2)
        v2 = min(a1, a2)
        v3 = v1 % v2
        if v3 == 0:
            return v2
        else:
            return gdc(v2, v3)
    v3 = False
    v4 = False
    v5 = v2[0]
    for v6 in v2:
        v5 = gdc(v5, v6)
        if v5 == 1:
            v3 = True
    if not v3:
        print('not coprime')
        exit()
    v7 = [0] * (10 ** 6 + 1)
    for v6 in v2:
        v7[v6] = 1
    v4 = all([sum(v7[i::i]) <= 1 for v8 in range(2, 10 ** 6 + 1)])
    if v4:
        print('pairwise coprime')
    elif v3:
        print('setwise coprime')
if __name__ == '__main__':
    f1()
