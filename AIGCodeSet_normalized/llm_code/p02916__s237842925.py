v1 = int(input())
v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = list(map(int, input().split()))
v5 = sum(v3)
for v6 in range(1, v1):
    if v2[v6] == v2[v6 - 1] + 1:
        v5 += v4[v2[v6] - 2]
print(v5)
