v1 = input()
v2 = 0
v3 = [int(i) for v4 in v1]
v3.reverse()

def f1(a1):
    if a1 >= len(v1):
        return true
    v1 = v3[a1]
    if v1 < 5:
        return false
    elif v1 > 5:
        v3[a1] = 10 - v3[a1]
        v3[a1 + 1] += 1
        return true
    elif f1(a1):
        pass
for v4 in range(len(v1) - 1):
    v5 = v3[v4]
    if v5 < 5:
        pass
    elif v5 > 5:
        v3[v4] = 10 - v3[v4]
        v3[v4 + 1] += 1
    elif v3[v4 + 1] >= 5:
        v3[v4] = 10 - v3[v4]
        v3[v4 + 1] += 1
    else:
        pass
v6 = len(v1) - 1
v2 = 0
if v3[v6] > 5:
    v3[v6] = 10 - v3[v6]
    v2 = 1
print(sum(v3) + v2)
