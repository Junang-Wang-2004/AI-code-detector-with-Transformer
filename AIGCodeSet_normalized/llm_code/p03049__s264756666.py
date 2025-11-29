v1 = int(input())
v2 = 0
v3 = 0
v4 = 0
v5 = 0
for v6 in range(v1):
    v7 = input()
    v2 += v7.count('AB')
    if v7[-1] == 'A':
        v3 += 1
    if v7[0] == 'B':
        v4 += 1
    if v7[-1] == 'A' and v7[0] == 'B':
        v5 += 1
if v3 == v5 and v4 == v5:
    v8 = min(v3, v4) - 1
else:
    v8 = min(v3, v4)
print(v2 + v8)
