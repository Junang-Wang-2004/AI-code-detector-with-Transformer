import numpy
v1, v2 = map(int, input().split())
v3 = []
v4 = []
v5 = 0
for v6 in range(v1):
    v7, v8 = map(int, input().split())
    v3.append(v7)
    v4.append(v8)
    if numpy.sqrt(v7 ** 2 + v8 ** 2) <= v2:
        v5 += 1
print('{}'.format(v5))
