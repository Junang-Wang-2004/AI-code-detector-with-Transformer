import sys
v1 = list(input())
v2 = 0
for v3 in range(len(v1)):
    if v3 >= 1:
        if v1[v3] == v1[v3 - 1]:
            if v1[v3 - 1] == '0':
                v1[v3] = '1'
            else:
                v1[v3] = '0'
            v2 += 1
print(v2)
