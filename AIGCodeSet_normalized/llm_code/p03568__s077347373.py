v1 = int(input().strip())
v2 = list(map(int, input().strip().split(' ')))
v3 = len([a for v4 in v2 if v4 % 2 == 0])
v5 = 3 ** v1 - 2 ** v3
print(v5)
