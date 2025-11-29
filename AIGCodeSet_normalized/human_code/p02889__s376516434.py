import sys
v1 = sys.stdin.buffer.read
v2 = sys.stdin.buffer.readline
v3 = sys.stdin.buffer.readlines
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
v4, v5, v6 = [int(_) for v7 in v2().split()]
v8 = np.array(v1().split(), dtype=np.int64)
v9 = v8[:3 * v5]
v10 = v8[3 * v5 + 1:]
v11, v12, v13 = (v9[::3], v9[1::3], v9[2::3])
v14, v15 = (v10[::2], v10[1::2])
v16 = csr_matrix((v13, (v11, v12)), shape=(v4 + 1, v4 + 1))
v17 = floyd_warshall(v16, directed=0)
v18 = np.full((v4 + 1, v4 + 1), np.inf)
np.fill_diagonal(v18, 0)
v18[v17 <= v6] = 1
v19 = floyd_warshall(v18, directed=0)
v19[v19 == np.inf] = 0
print('\n'.join((v19.astype(int)[v14, v15] - 1).astype(str)))
