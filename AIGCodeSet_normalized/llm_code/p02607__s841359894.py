from sys import stdin
input = stdin.readline
v1 = int(input().rstrip())
v2 = [int(x) for v3 in input().split()]
v4 = 0
for v5 in range(v1):
    if v5 % 2 != 0 and v2[v5] % 2 != 0:
        v4 = v4 + 1
print(v4)
