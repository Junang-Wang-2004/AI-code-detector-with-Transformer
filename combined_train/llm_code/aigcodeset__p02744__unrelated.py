def f1(a1, a2):
    if len(a1) != len(a2):
        return False
    v1 = {}
    for v2 in range(len(a1)):
        if a1[v2] in v1:
            if v1[a1[v2]] != a2[v2]:
                return False
        else:
            if a2[v2] in v1.values():
                return False
            v1[a1[v2]] = a2[v2]
    return True

def f2(a1):
    for v1 in range(len(a1)):
        for v2 in range(v1 + 1, len(a1)):
            if a1[v1] == a1[v2] and a1[v1] < a1[v2]:
                return False
    return True

def f3(a1):
    v1 = []

    def backtrack(a1, a2):
        if len(a1) == a1:
            if f2(a1):
                v1.append(a1)
            return
        for v1 in range(26):
            v2 = chr(ord('a') + v1)
            if v2 not in a2:
                a2.add(v2)
                backtrack(a1 + v2, a2)
                a2.remove(v2)
    backtrack('', set())
    return v1
v1 = int(input())
v2 = f3(v1)
for v3 in v2:
    print(v3)
