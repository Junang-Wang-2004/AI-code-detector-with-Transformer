def f1(a1, a2):
    while a1 % a2 != 0:
        v1 = a1
        a1 = a2
        a2 = v1 % a2
    return a2
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in range(v1):
    v5 = v2[:v4] + v2[v4 + 1:]
    v5.append(1)
    v6 = v5[0]
    for v7 in v5:
        v6 = f1(v6, v7)
    if v6 > v3:
        v3 = v6
print(v3)
