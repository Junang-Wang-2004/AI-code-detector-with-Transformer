v1 = input()
v2 = int(input())
v3 = len(v1)
v4 = set(list(v1))
for v5 in range(v2):
    for v6 in range(v3 - v5):
        v4.add(v1[v6:v6 + v5 + 1])
v4 = list(v4)
v4.sort()
print(v4[v2 - 1])
