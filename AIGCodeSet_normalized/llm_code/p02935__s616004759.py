import itertools as it
import numpy as np
from copy import deepcopy

def f1():
    v1 = [input() for v2 in range(2)]
    v3 = int(v1[0])
    v4 = [float(i) for v5 in v1[1].split(' ')]
    v6 = [list(it.combinations(range(l), 2)) for v7 in range(2, len(v4) + 1)]
    v6.reverse()
    v8 = np.empty((np.prod([len(c) for v9 in v6]), len(v6)), dtype='i')
    for v5, v10 in enumerate(v6):
        v8[:, v5] = np.array(list(range(len(v10))) * int(len(v8) / len(v10)))
    v11 = 0.0
    for v12 in v8:
        v13 = []
        v14 = deepcopy(v4)
        for v15, v5 in enumerate(v12):
            v13.append(v6[v15][v5])
        for v16 in v13:
            v5, v17 = v16
            v18 = (v14.pop(max(v5, v17)) + v14.pop(min(v5, v17))) / 2.0
            v14.append(v18)
        if v11 < v14[0]:
            v11 = v14[0]
    print(v11)
if __name__ == '__main__':
    f1()
