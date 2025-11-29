v1 = int(input())
v2 = list(map(int, input().split()))
v3 = sum([1 for v4 in v2 if v4 % 2 != 0])
print(3 ** v1 - 2 ** v3)
