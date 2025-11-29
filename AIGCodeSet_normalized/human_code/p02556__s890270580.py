v1 = int(input())
v2 = []
v3 = []
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    v2.append(v5 + v6)
    v3.append(v5 - v6)
print(max(max(v2) - min(v2), max(v3) - min(v3)))
