v1 = input()
v2 = len(v1)
v3 = int(input())
v4 = set()
for v5 in range(1, v2 + 1):
    for v6 in range(v2 - v5 + 1):
        v4.add(v1[v6:v6 + v5])
v4 = sorted(list(v4))
print(v4[v3 - 1])
