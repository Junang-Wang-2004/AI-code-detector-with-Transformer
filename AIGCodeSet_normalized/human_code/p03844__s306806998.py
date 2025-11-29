v1, v2, v3 = map(str, input().split())
v4 = int(v1)
v5 = int(v3)
v6 = 0
if v2 == '+':
    v6 = v4 + v5
else:
    v6 = v4 - v5
print(v6)
