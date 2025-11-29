v1, v2 = (input(), input())
v3, v4 = (len(v1), len(v2))
v5 = ''
for v6 in range(v4):
    v5 += v1[v6] + v2[v6]
if v3 - v4:
    v5 += v1[-1]
print(v5)
