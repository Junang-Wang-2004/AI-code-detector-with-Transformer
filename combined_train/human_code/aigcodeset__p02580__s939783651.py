import os
import sys
from atexit import register
from io import BytesIO
sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))
input = lambda: sys.stdin.readline().rstrip('\r\n')
v1 = lambda: sys.stdin.readline().rstrip('\r\n')
v2, v3, v4 = (int(x) for v5 in input().split())
v6 = [[0, i] for v7 in xrange(v2)]
v8 = [[0, v7] for v7 in xrange(v3)]
v9 = dict()
for v7 in xrange(v4):
    v10, v11 = (int(v5) - 1 for v5 in input().split())
    v6[v10][0] += 1
    v8[v11][0] += 1
    v9[v10, v11] = True
v6 = sorted(v6, reverse=True)
v8 = sorted(v8, reverse=True)
v12 = 1
for v13 in v6:
    v14 = None
    for v15 in v8:
        v16 = v9.get((v13[1], v15[1]), False)
        if v16 and v14 is None:
            v14 = v13[0] + v15[0] - 1
            v17 = v14
        elif v16 and v13[0] + v15[0] - 1 < v14:
            v17 = v14
            break
        elif v16:
            pass
        else:
            if v14 is None:
                v17 = v13[0] + v15[0]
            else:
                v17 = max(v13[0] + v15[0], v14)
            break
    if v17 > v12:
        v12 = v17
    if v17 < v12:
        break
print(v12)
