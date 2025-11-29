v1 = input()
v2 = 0
v3 = 0
v4 = False
for v5 in list(v1):
    if v5 == 'A' and v4 == False:
        v4 = True
        v2 += 1
    elif v5 == 'Z' and v4:
        v2 += 1
        v4 = False
        v3 = max(v3, v2)
        v2 = 0
    elif v4:
        v2 += 1
    else:
        v2 = 0
print(v3)
