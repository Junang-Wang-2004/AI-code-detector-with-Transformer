v1 = int(input())
v2 = 1
v3 = 1
v4 = 1000000007
for v5 in range(v1 - 1):
    v2 = v2 * 10 % v4
    v3 = v3 * 8 % v4
v2 = (v2 * 9 - v3 * 3 + v4) % v4
print(v2)
