import numpy as np
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = np.array(list(map(int, input().split())))
v5 = 10 ** 9 + 7
v6 = np.ones(v2 + 1, dtype='int64')
for v7 in v3:
    v6[1:] = ((v6[:-1] * (v7 == v4)).cumsum() + v6[1:]) % v5
    print(v6)
print(v6[-1])
