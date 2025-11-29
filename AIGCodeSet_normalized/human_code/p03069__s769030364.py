v1 = int(input())
v2 = input()
v3 = 1 << 40
v4 = 0
v5 = v2.count('.')
for v6 in range(v1):
    v3 = min(v3, v4 + v5)
    if v2[v6] == '.':
        v5 -= 1
    else:
        v4 += 1
v3 = min(v3, v4 + v5)
print(v3)
