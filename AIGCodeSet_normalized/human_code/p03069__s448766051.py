v1 = int(input())
v2 = input()
v3, v4 = (0, v2.count('.'))
v5 = [v4]
for v6 in range(v1):
    if v2[v6] == '#':
        v3 += 1
    else:
        v4 -= 1
    v5.append(v3 + v4)
print(min(v5))
