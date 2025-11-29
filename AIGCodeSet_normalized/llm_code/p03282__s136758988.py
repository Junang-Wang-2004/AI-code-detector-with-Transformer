v1 = input()
v2 = int(input())
v3 = 0
if len(v1) == 1:
    v3 = v1[0]
else:
    v4 = 0
    while v4 < len(v1) and v1[v4] == '1':
        v4 += 1
    v3 = v1[v4]
print(v3)
