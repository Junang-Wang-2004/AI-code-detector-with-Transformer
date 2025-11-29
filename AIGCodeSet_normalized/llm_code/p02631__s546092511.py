from functools import reduce
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = reduce(lambda a, b: a ^ b, v2)
v4 = map(lambda x: x ^ v3, v2)
print(*v4)
