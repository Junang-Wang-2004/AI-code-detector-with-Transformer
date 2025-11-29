v1 = input()
v2 = int(input())
v3 = set()
for v4 in range(len(v1)):
    for v5 in range(v4 + 1, len(v1) + 1):
        v3.add(v1[v4:v5])
v6 = sorted(list(v3))
print(v6[v2 - 1])
