v1 = int(input())
v2 = 0
v3 = 0
v4 = 0
if v1 % 2 == 0:
    for v5 in range(1, 19):
        v2 += v1 // 10 ** v5
v6 = v1 // 10
for v5 in range(1, 26):
    v3 += v6 // 5 ** v5
for v5 in range(1, 18):
    v4 += v6 // 2 ** v5
v2 += min(v3, v4)
print(v2)
