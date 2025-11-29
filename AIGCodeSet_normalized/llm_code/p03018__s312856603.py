v1 = input()
v2 = 0
for v3 in range(len(v1) - 2):
    if v1[v3] + v1[v3 + 1] + v1[v3 + 2] == 'ABC':
        v2 += 1
        v1 = v1[:v3] + 'BCA' + v1[v3 + 3:]
print(v2)
