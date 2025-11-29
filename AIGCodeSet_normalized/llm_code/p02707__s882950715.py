v1 = int(input())
v2 = list(map(int, input().split()))
v3 = [0] * v1
for v4 in v2:
    v3[v4 - 1] += 1
for v5 in v3:
    print(v5)
