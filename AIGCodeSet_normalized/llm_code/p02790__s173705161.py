v1, v2 = map(int, input().split())
v3 = ''
v4 = ''
for v5 in range(v2):
    v3 += str(v1)
for v5 in range(v1):
    v4 += str(v2)
print(v3 if v3 <= v4 else v4)
