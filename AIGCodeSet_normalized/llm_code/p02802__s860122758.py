import numpy as np
v1, v2 = map(int, input().split())
v3 = np.zeros((v1 + 1, 2), dtype=np.int16)
for v4 in range(v2):
    v5, v6 = input().split()
    v5 = int(v5)
    if v3[v5][0] == 0:
        if v6 == 'AC':
            v3[v5][0] += 1
        elif v6 == 'WA':
            v3[v5][1] += 1
print('%d %d' % (v3[1:, 0].sum(), v3[1:, 1].sum()))
