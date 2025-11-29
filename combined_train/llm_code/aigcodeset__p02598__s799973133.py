v1, v2 = map(int, input().split())
v3 = input().split()
max = 0
for v4 in range(v1):
    v3[v4] = int(v3[v4])
    if max <= v3[v4]:
        max = v3[v4]
v5 = 1
v6 = max

def f1(a1):
    v1 = 0
    for v2 in range(v1):
        v1 += -(-1 * v3[v2] // a1) - 1
    return v1
while v6 - v5 > 1:
    if v2 == 0:
        break
    if f1((v6 + v5) // 2) > v2:
        v5 = (v6 + v5) // 2
    else:
        v6 = (v6 + v5) // 2
print(v6)
