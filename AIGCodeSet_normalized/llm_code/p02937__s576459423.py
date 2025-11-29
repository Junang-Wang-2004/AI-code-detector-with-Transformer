v1 = input()
v2 = input()
v3 = 0
v4 = 0
while v4 < len(v2):
    if v3 == len(v1):
        v3 = 0
    if v1[v3] == v2[v4]:
        v4 += 1
    v3 += 1
if v4 == len(v2):
    print(v3)
else:
    print(-1)
