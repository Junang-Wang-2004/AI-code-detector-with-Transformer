v1 = int(input())

def f1():
    v1 = 0
    v2 = v1 - 1
    print(v1, flush=True)
    v3 = input()
    if v3 == 'Vacant':
        return
    print(v2, flush=True)
    v4 = input()
    if v4 == 'Vacant':
        return
    while v1 < v2:
        v5 = (v1 + v2) // 2
        print(v5, flush=True)
        v6 = input()
        if v6 == 'Vacant':
            return
        if not (v1 ^ v5) & 1 and v3 == v6 or ((v1 ^ v5) & 1 and v3 != v6):
            v1 = v5
            v3 = v6
        else:
            v2 = v5
f1()
