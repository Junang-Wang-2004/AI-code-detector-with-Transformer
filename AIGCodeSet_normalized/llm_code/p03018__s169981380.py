v1 = input()
v2 = 0
v3 = 0
while v3 < len(v1) - 2:
    if v1[v3:v3 + 3] == 'ABC':
        v2 += 1
        v1 = v1[:v3] + 'BCA' + v1[v3 + 3:]
        v3 += 2
    else:
        v3 += 1
print(v2)
