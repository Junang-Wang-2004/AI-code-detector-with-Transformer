v1, v2 = map(int, input().split())
v3 = min(v1, v2)
v4 = max(v1, v2)
v5 = [str(v3)] * v4
print(''.join(v5))
