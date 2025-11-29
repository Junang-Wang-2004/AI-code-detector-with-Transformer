v1, v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = max(v3)
print(max(v4 - (v1 - v4 + 1), 0))
