v1 = int(input())
v2 = list(map(int, input().split()))
v3 = []
for v4 in range(v1):
    if v4 + 1 < v2[v4]:
        v3 = [0] * 1
        v3[0] = -1
        break
    v3.insert(v2[v4] - 1, v2[v4])
for v5 in range(v1):
    print(v3[v5])
