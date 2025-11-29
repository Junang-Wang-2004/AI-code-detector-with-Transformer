v1 = int(input())
v2 = []
for v3 in range(v1):
    v2.append(int(input()))
v2.sort()
v4 = 0
while len(v2) > 1:
    v5 = v2.pop(0)
    v6 = v2.pop(0)
    v2.append((v5 + v6) / 2)
    v2.sort()
print(v2[0])
