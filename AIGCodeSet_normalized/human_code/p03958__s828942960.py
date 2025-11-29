v1, v2 = map(int, input().split())
*v3, = map(int, input().split())
v4 = max(v3)
print(max(0, v4 - (v1 - v4 + 1)))
