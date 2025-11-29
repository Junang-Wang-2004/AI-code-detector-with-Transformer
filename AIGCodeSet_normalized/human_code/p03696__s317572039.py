from functools import reduce
v1 = int(input())
v2 = input()
v3, v4 = reduce(lambda acc, s: (acc[0] + 1 if s == '(' else max(0, acc[0] - 1), acc[1] + 1 if s == ')' and acc[0] == 0 else acc[1]), v2, (0, 0))
v5 = v4 * '(' + v2 + v3 * ')'
print(v5)
