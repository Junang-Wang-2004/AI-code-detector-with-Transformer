v1 = input()
v2 = input()
v3 = min(len(v1), len(v2))
v4 = ''
for v5 in range(v3):
    v4 = v4 + v1[v5] + v2[v5]
if len(v1) > len(v2):
    v4 = v4 + v1[len(v1)]
print(v4)
