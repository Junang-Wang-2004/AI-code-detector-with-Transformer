v1, v2, *v3 = map(int, open((v4 := 0)).read().split())
v3.sort()
v5 = v6 = ~v2 % 2 or v3.pop()
v7 = 1
for v8 in v2 // 2 * '_':
    if (v9 := (v3[v4] * v3[v4 + 1])) * v6 > (v10 := (v3[-v7] * v3[~v7])) * v6:
        v5 *= v9
        v4 += 2
    else:
        v5 *= v10
        v7 += 2
    v5 %= 10 ** 9 + 7
print(v5)
