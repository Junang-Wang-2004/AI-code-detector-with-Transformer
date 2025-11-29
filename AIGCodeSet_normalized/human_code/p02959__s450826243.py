def f1():
    return [int(s) for v1 in input().split()]
v1 = int(input())
v2 = f1()
v3 = f1()
v4 = 0
for v5 in range(v1):
    if v2[v5] > v3[v5]:
        v4 += v3[v5]
    elif v3[v5] < v2[v5] + v2[v5 + 1]:
        v4 += v3[v5]
        v2[v5 + 1] = v2[v5 + 1] - (v3[v5] - v2[v5])
    else:
        v4 += v2[v5] + v2[v5 + 1]
        v2[v5 + 1] = 0
print(v4)
