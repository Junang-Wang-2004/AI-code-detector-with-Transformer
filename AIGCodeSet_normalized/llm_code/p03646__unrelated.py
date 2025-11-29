v1 = int(input())
v2 = [1000] * 50
for v3 in range(49, -1, -1):
    if v1 >= v3:
        v2[v3] += v1 // v3
        v1 %= v3
v4 = 50
while v4 > 0 and v2[v4 - 1] == 1000:
    v4 -= 1
print(v4)
print(*v2[:v4])
