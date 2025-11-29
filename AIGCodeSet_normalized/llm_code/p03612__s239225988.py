v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0

def f1(a1):
    global c
    v1 = v2[a1 + 1]
    v2[a1 + 1] = v2[a1]
    v2[a1] = v1
    v2 += 1
for v4 in range(v1 - 1):
    if v2[v4] == v4 + 1:
        f1(v4)
        if v2[v4 + 1] == v4 + 2:
            f1(v4 + 1)
print(v3)
