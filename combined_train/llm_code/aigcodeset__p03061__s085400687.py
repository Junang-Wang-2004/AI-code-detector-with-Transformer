v1 = int(input())
v2 = input().split()
for v3 in range(v1):
    v2[v3] = int(v2[v3])
v2.sort(reverse=True)
v4 = [v2[v3] for v3 in range(v1)]

def f1(a1, a2):
    if a2 == 0:
        return a1
    return f1(a2, a1 % a2)

def f2(a1):
    v1 = 1
    if len(a1) == 1:
        return a1[0]
    elif len(a1) == 2:
        return max(a1[0], a1[1])
    else:
        v2 = f1(a1[0], a1[1])
        v3 = f1(a1[len(a1) - 3], a1[len(a1) - 1])
        v4 = max(v2, v3)
        for v5 in range(2, len(a1)):
            v4 = f1(v4, a1[v5])
            if f1(v4, a1[v5]) > v1:
                v1 = v4
        return v1
v5 = 0
v6 = 0
print(max(v4[0], f2(v4[1:])))
