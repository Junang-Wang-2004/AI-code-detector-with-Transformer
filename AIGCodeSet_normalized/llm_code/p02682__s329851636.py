v1, v2, v3, v4 = map(int, input().split())
v5 = [1] * v1 + [0] * v2 + [-1] * v3
print(sum(v5[0:v4]))
