v1 = 'keyence'
v2 = [[v1[:i], v1[i:]] for v3 in range(0, len(v1))]

def f1(a1):
    for v1 in v2:
        if v1[0] + v1[1] == a1:
            return 'YES'
    return 'NO'
v4 = input()
print(f1(v4))
