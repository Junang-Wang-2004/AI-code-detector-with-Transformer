v1, v2, v3, v4 = map(int, input().split())
v5 = min(v1, v4)
v4 -= v5
v5 += min(v2, v4)
v4 -= min(v2, v4)
v5 -= min(v3, v4)
print(v5)
