v1 = 10 ** 9 + 7
v2 = int(input())
v3 = list(map(int, input().split()))
v4 = 0
v5 = sum(v3)
for v6 in v3:
    v4 = (v4 + (v5 - v6) * v6) % v1
v4 = v4 * pow(2, v1 - 2, v1) % v1
print(v4)
