import numpy as np
v1 = int(input())
v2 = list(map(int, input().split()))
v2 = np.array(v2) % (10 ** 9 + 7)
v3 = v2.reshape(1, -1)
v4 = np.dot(v3, v3.T) % (10 ** 9 + 7)
v5 = int((np.sum(v4) - np.sum(np.diag(v4))) / 2 % (10 ** 9 + 7))
print(v5)
