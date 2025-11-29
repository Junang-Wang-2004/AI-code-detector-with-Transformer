v1 = int(input())
v2 = 0
v3 = 0
v4 = 0
v5 = []
for v6 in range(v1):
    v7 = input()
    v5.append(v7)
    v4 += v7.count('AB')
    if v7[0] == 'B':
        v2 += 1
    if v7[-1] == 'A':
        v3 += 1
v4 += min(v2, v3)
print(v4)
