import numpy as np
v1, v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v3 = np.sort(v3)[::-1]
v3 = v3[:int(np.sqrt(v2) + 1)]
v4 = int(min(v2, len(v3)))
v5 = np.zeros(1)
v5 = np.append(v5, [[a] + v3 for v6, v7 in enumerate(v3) if v6 <= v4])
v5 = np.sort(v5)[::-1][:v2]
print(int(sum(v5[:v2])))
