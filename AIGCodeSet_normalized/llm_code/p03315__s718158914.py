v1 = list(input())
v2 = 0
for v3 in v1:
    if v3 == '+':
        v2 += 1
    elif v3 == '-':
        v2 -= 1
print(v2)
