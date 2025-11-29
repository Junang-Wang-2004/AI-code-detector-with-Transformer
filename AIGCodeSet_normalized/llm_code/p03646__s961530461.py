v1 = int(input())
v2 = 50
v3 = [0] * v2
for v4 in range(v2):
    v3[v4] = v1 // v2
    v1 %= v2
for v4 in range(v2 - 1, v2 - 1 - v1, -1):
    v3[v4] += 1
print(v2)
print(*v3)
