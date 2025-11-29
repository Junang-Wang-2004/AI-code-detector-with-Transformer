v1 = int(input())
v2 = [0] * 3
for v3 in range(v1):
    v4, v5, v6 = map(int, input().split())
    v2 = [v4 + max(v2[1], v2[2]), v5 + max(v2[0], v2[2]), v6 + max(v2[0], v2[1])]
print(max(v2))
