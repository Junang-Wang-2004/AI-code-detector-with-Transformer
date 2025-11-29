v1 = input()
v2 = int(input())
v3 = set()
for v4 in range(1, v2 + 1):
    for v5 in range(len(v1) - v4 + 1):
        v3.add(v1[v5:v5 + v4])
v3 = sorted(v3)
print(v3[v2 - 1])
