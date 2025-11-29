v1 = input()
v2 = list(v1)
v3 = 0
for v4 in v2:
    if v4 == '+':
        v3 += 1
print(v3 - (len(v2) - v3))
