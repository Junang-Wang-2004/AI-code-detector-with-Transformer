v1 = int(input())
v2 = 10 ** 9 + 7
v3 = pow(4, v1 - 2, v2) * (v1 - 2) * 3
v4 = pow(4, v1 - 3, v2) * (v1 - 3) * 6
v5 = pow(4, v1, v2)
print((v5 - v3 - v4) % v2)
