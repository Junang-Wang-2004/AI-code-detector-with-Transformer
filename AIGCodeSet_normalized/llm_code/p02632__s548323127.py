import math
v1 = 10 ** 9 + 7
v2 = int(input())
v3 = input()
v4 = math.comb(v2 + len(v3), v2) * pow(26, v2, v1)
print(v4 % v1)
