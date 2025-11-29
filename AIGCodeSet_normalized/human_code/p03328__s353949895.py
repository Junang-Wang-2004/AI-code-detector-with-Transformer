v1 = input().split()
v2 = int(v1[0])
v3 = int(v1[1])
v4 = 0
for v5 in range(v3 - v2):
    v4 += v5
print(v4 - v2)
