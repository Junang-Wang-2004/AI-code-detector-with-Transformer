v1, v2 = map(int, input().split())
'\nPC = []\nfor i in range(d):\n    pc = list(map(int,input().split()))\n    PC.append(pc)\n'
v3 = [list(map(int, input().split())) for v4 in range(v1)]

def f1(a1, a2):
    if a2 <= 0:
        return float('inf')
    v1 = min(int(a1 / 100 * a2), v3[a2 - 1][0])
    v2 = 100 * a2 * v1
    if v1 == v3[a2 - 1][0]:
        v2 += v3[a2 - 1][1]
    return v1 + f1(a1 - v2, a2 - 1)
print(f1(v2, v1))
