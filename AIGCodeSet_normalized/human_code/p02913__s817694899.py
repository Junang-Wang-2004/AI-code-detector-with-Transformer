v1 = int(input())
v2 = input()
v3 = [0] * v1
v4 = 0
for v5 in range(v1):
    while v2[v5:v4] in v2[v4:v1]:
        v3[v5] = v4 - v5
        v4 += 1
print(max(v3))
