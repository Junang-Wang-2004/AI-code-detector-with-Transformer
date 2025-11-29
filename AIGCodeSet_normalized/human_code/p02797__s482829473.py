v1, v2, v3 = map(int, input().split())
if v3 != int(1000000000.0):
    v4 = [int(1000000000.0)] * v1
    for v5 in range(v2):
        v4[v5] = v3
    for v5 in range(len(v4)):
        print(v4[v5])
else:
    v4 = [1] * v1
    for v5 in range(v2):
        v4[v5] = v3
    for v5 in range(len(v4)):
        print(v4[v5])
