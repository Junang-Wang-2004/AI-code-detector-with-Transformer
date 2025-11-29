v1 = int(input())
v2 = []
v3 = 0
for v4 in range(v1):
    v2.append(int(input()))
    if v2[v4] % 2 == 0:
        v3 += 1
if v3 == v1:
    v5 = 'second'
else:
    v5 = 'first'
print(v5)
