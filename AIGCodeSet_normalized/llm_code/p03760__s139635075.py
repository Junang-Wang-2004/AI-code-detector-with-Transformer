v1 = input()
v2 = input()
v3 = ''
for v4 in range(len(v1)):
    v3 += v1[v4]
    if v4 < len(v2):
        v3 += v2[v4]
print(v3)
