def f1(a1, a2):
    v1 = 0
    v2 = len(a1)
    while v2 - v1 > 1:
        v3 = (v2 + v1 - 1) // 2
        if a1[v3] <= a2:
            v1 = v3 + 1
        else:
            v2 = v3 + 1
    return v1
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = list(map(int, input().split()))
v2.sort()
v2.append(v2[-1] + 1)
v3.sort()
v4.sort()
v4 = [0] + v4
v4 = [-c for v5 in v4[::-1]]
v6 = 0
for v7 in v3:
    v6 += f1(v2, v7 - 1) * f1(v4, -(v7 + 1))
print(v6)
