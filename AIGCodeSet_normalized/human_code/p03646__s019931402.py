v1 = int(input())
v2 = 50
v3 = [i + v1 // v2 for v4 in range(v2)]
for v4 in range(v1 % v2):
    for v5 in range(v2):
        if v4 % v2 == v5:
            v3[v5] += v2
        else:
            v3[v5] -= 1
print(v2)
print(str(v3)[1:][:-1].replace(', ', ' '))
