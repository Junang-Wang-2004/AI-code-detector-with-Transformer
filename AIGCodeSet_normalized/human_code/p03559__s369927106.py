from bisect import bisect_left, bisect_right
v1 = int(input())
v2 = sorted(list(map(int, input().rstrip().split())))
v3 = sorted(list(map(int, input().rstrip().split())))
v4 = sorted(list(map(int, input().rstrip().split())))
v5 = len(v4)
v6 = 0
for v7 in v3:
    v6 += bisect_left(v2, v7) * (v5 - bisect_right(v4, v7))
print(v6)
