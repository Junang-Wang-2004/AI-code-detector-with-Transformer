import numpy
v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    v3.append((v5, v6))
v7 = numpy.zeros(v2, dtype=int)
v3.sort()
v8 = 0
for v9, v10 in v3:
    v8 = max(v8, v7[-1] + v10)
    v7[v9:] = numpy.maximum(v7[v9:], v7[:-v9] + v10)
print(v8)
