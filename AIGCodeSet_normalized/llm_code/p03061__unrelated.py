def f1(a1, a2):
    while a2:
        a1, a2 = (a2, a1 % a2)
    return a1
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 1
for v4 in range(v1):
    for v5 in range(v4 + 1, v1):
        v3 = max(v3, f1(v2[v4], v2[v5]))
print(v3)
