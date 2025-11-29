v1 = int(input())
v2 = [0 for v3 in range(v1)]
v4 = list(map(int, input().split()))
for v5 in range(v1 - 1):
    v2[v4[v5] - 1] += 1
for v6 in range(v1):
    print(v2[v6])
