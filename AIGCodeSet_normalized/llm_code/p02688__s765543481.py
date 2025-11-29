v1, v2 = map(int, input().split())
v3 = [0] * v1
for v4 in range(v2):
    v5 = int(input())
    v6 = list(map(int, input().split()))
    for v7 in v6:
        v3[v7 - 1] += 1
print(v3.count(0))
