v1 = int(input())
v2 = 0
for v3 in range(v1):
    v4, v5 = input().split()
    v4 = float(v4)
    if v5 == 'BTC':
        v4 *= 380000.0
    v2 += v4
print(v2)
