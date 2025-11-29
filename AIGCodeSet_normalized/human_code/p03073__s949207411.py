v1 = input()
v2 = 0
v3 = 0
v2 += v1[::2].count('0')
v2 += v1[1::2].count('1')
v3 += v1[::2].count('1')
v3 += v1[1::2].count('0')
print(min(v2, v3))
