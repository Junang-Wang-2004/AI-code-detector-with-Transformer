v1, v2, v3, v4 = map(int, input().split())
import numpy as np
v5 = np.array([[0, -1], [1, 0]])
v6 = np.array([v1, v2])
v7 = np.array([v3 - v1, v4 - v2])
v8 = v5 @ v7
v9 = v6 + v8
v10 = v9 + v7
print(*v10, *v9)
