v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v3.append(v4 + 1)
for v5 in range(v2):
    v6 = int(input())
    v7 = list(map(int, input().split()))
    for v4 in v7:
        if v4 in v3:
            v3.remove(v4)
print(len(v3))
