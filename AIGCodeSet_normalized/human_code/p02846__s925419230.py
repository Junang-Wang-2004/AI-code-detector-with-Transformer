import sys
input = sys.stdin.readline
v1, v2 = list(map(int, input().split()))
v3, v4 = list(map(int, input().split()))
v5, v6 = list(map(int, input().split()))
v7 = v3 * v1
v8 = v7 + v4 * v2
v9 = v5 * v1
v10 = v9 + v6 * v2
if v8 == v10:
    v11 = 'infinity'
elif (v7 - v9) * (v8 - v10) > 0:
    v11 = 0
else:
    v12 = abs(v7 - v9)
    v13 = abs(v8 - v10)
    v14 = v12 // v13
    v15 = v12 % v13
    if v15 == 0:
        v11 = v14 * 2
    else:
        v11 = v14 * 2 + 1
print(v11)
