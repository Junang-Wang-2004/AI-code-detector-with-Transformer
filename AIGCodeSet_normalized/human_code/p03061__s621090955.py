v1 = int(input())
v2 = list(map(int, input().split()))

def f1(a1, a2):
    while a2 != 0:
        a1, a2 = (a2, a1 % a2)
    return a1
v3 = [0] * v1
v4 = [0] * (v1 + 1)
v5 = [0] * (v1 + 1)
for v6 in range(v1):
    v4[v6 + 1] = f1(v4[v6], v2[v6])
for v6 in range(v1):
    v5[v6 + 1] = f1(v5[v6], v2[v1 - v6 - 1])
for v6 in range(v1):
    v3[v6] = f1(v4[v6], v5[v1 - v6 - 1])
print(max(v3))
