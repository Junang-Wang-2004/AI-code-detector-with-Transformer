v1 = input()
sum = 0
v2 = v1[0]
if len(v1) != 1:
    for v3 in range(1, len(v1)):
        if v1[v3] == v2[v3 - 1]:
            sum += 1
            if v1[v3] == '1':
                v2 += '0'
            else:
                v2 += '1'
        else:
            v2 += v1[v3]
print(sum)
