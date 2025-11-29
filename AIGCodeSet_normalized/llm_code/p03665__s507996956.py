from scipy.special import comb
from collections import deque
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = v3.count(0)
v5 = v3.count(1)
if v2 == 0:
    v6 = [0] + [2 * x for v7 in range(1, (v5 + 2) // 2)]
if v2 == 1:
    v6 = [1] + [2 * v7 + 1 for v7 in range(1, (v5 + 1) // 2)]
v8 = deque(v6)
v9 = 0
while v8:
    v10 = v8.popleft()
    v11 = comb(v5, v10, exact=True)
    v9 += v11
print(2 ** v4 * v9)
