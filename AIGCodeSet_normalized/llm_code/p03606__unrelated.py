v1 = int(input())
v2 = set()
for v3 in range(v1):
    v4, v5 = map(int, input().split())
    for v6 in range(v4, v5 + 1):
        v2.add(v6)
print(len(v2))
