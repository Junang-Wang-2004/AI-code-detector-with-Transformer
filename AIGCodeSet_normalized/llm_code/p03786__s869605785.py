v1 = int(input())
v2 = input()
v2 = v2.split(' ')
v3 = [(i, int(v2[i])) for v4 in range(v1)]
v3.sort(key=lambda x: x[1])
v5 = 0
v6 = v3[0][1]
for v4 in range(1, v1):
    if v6 * 2 >= v3[v4][1]:
        v6 += v3[v4][1]
    else:
        break
for v4 in range(v1):
    if v6 * 2 >= v3[v4][1]:
        v5 += 1
print(v5)
