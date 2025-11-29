v1 = input()
v2 = v1[::2].count('0') + v1[1::2].count('1')
print(min(v2, len(v1) - v2))
