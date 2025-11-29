from bisect import bisect_right
v1 = int(input())
v2 = input()
v3 = 0
v4 = [[] for v5 in range(10)]

def f1(a1, a2):
    """Find leftmost value greater than x"""
    v1 = bisect_right(a1, a2)
    if v1 != len(a1):
        return a1[v1]
    return None
for v6 in range(v1):
    v4[int(v2[v6])].append(v6)
for v7 in range(1000):
    v8 = '000' + str(v7)
    v8 = v8[-3:]
    v9, v10, v11 = map(int, tuple(v8))
    v12 = -1
    v12 = f1(v4[v9], v12)
    if v12 is None:
        continue
    v13 = f1(v4[v10], v12)
    if v13 is None:
        continue
    v14 = f1(v4[v11], v13)
    if v14 is None:
        continue
    v3 += 1
print(v3)
