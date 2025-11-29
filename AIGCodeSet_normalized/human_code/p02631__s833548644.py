from functools import reduce
v1 = int(input())
v2 = list(map(int, input().split()))
all = reduce(lambda x, y: x ^ y, v2)
v3 = [all ^ i for v4 in v2]
print(*v3)
