v1 = str(input())
v2 = 0
if len(v1) >= 99:
    for v3 in range(len(v1)):
        v2 += min(10 - int(v1[v3]), int(v1[v3]))
else:
    for v3 in range(len(v1)):
        v2 += min(10 - int(v1[v3]), int(v1[v3])) + 1
print(v2)
