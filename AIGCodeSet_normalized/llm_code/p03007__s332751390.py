v1 = int(input())
v2 = list(map(int, input().split(' ')))
v2.sort()
v3 = []
for v4 in range(v1 - 1):
    v5 = v2.pop()
    v6 = v2.pop()
    v2.insert(0, v5 - v6)
    v3.append((v5, v6))
v7 = v2[0]
print(v7)
for v4 in v3:
    print(v4[0], v4[1])
