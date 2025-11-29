v1 = []
v2, v3 = map(int, input().split())
for v4 in range(max(v2, v3)):
    v1.append(min(v2, v3))
print(''.join(map(str, v1)))
