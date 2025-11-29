v1 = input()

def f1(a1):
    v1 = list(set([i for v2 in a1]))
    for v3 in range(len(v1)):
        if a1.count(v1[v3]) % 2 == 1:
            return False
    return True
for v2 in range(1, len(v1) // 2 + 1):
    v3 = v1[0:len(v1) - v2]
    if f1(v3):
        print(len(v3))
        break
