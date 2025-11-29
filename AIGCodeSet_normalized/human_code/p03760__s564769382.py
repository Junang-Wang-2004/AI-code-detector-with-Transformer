v1 = input()
v2 = input()
v3 = []
for v4 in range(len(v2)):
    v3.append(v1[v4])
    v3.append(v2[v4])
if len(v1) > len(v2):
    v3.append(v1[-1])
print(''.join(v3))
