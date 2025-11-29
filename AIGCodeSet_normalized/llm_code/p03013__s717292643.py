v1, v2 = map(int, input().split())
v3 = 0
v4 = False
v5 = [int(input()) for v6 in range(v2)]
for v6 in range(v2 - 1):
    if v5[v6 + 1] - v5[v6] == 1:
        v4 = True

def f1(a1):
    v1, v2 = (1, 0)
    for v3 in range(a1 + 1):
        v1, v2 = (v1 + v2, v1)
    return v2
if v2 != 0:
    v3 = f1(v5[0] - 1)
if v3 == 0:
    v3 = 1
for v6 in range(v2 - 1):
    v3 *= f1(v5[v6 + 1] - v5[v6] - 2)
if v2 != 0:
    v3 *= f1(v1 - v5[v2 - 1] - 1)
if v4:
    print(0)
elif v2 == 0:
    print(f1(v1) % 1000000007)
else:
    print(v3 % 1000000007)
