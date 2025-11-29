v1 = list(input())
v2 = int(input())
v3 = 1
for v4 in range(v2):
    if int(v1[v4]) != 1:
        v3 = v1[v4]
        break
print(v3)
