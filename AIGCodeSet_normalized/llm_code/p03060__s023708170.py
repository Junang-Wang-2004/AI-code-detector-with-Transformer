from functools import reduce
import numpy as np
input()
v1 = np.array(list(map(int, input().split())))
v2 = np.array(list(map(int, input().split())))
print(reduce(lambda x, y: x + max(0, y), list(v1 - v2)))
