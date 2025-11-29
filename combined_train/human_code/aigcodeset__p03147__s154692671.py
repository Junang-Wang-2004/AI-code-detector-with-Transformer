def f1(a1):
    for v1 in range(N):
        if a1[v1] != 0:
            return False
    return True

def f2(a1):
    if a1 == N:
        return 0
    for v1 in range(a1, N):
        if h[v1] != 0:
            return v1
    return 0
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v4 = 0
v5 = 0
while not f1(v2):
    while v3 < v1 and v2[v3] != 0:
        v2[v3] -= 1
        v3 += 1
    if v3 != 0:
        v5 += 1
    v3 = f2(v3)
print(str(v5))
