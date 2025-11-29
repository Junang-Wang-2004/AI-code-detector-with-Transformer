v1 = int(input())
v2 = 10 ** v1 - (2 * 9 ** v1 - 8 ** v1)
v2 = v2 % (10 ** 9 + 7)
print(v2)
