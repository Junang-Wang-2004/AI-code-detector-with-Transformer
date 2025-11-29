v1 = input()
v2 = 0
for v3 in range(2 ** (len(v1) - 1)):
    v4 = ''
    for v5 in range(len(v1)):
        v4 += v1[v5]
        if v3 >> v5 & 1:
            v4 += '+'
    v2 += eval(v4)
print(v2)
