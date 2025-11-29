v1 = input()
v2 = input()
v3 = ''
if len(v1) > len(v2):
    for v4 in range(len(v2)):
        v3 += v1[v4] + v2[v4]
    v3 += v1[-1]
else:
    for v4 in range(len(v1)):
        v3 += v1[v4] + v2[v4]
print(v3)
