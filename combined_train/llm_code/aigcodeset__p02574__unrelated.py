def f1(a1):
    if len(a1) == 2:
        return f2(a1[0], a1[1]) == 1
    for v1 in range(len(a1)):
        for v2 in range(v1 + 1, len(a1)):
            if f2(a1[v1], a1[v2]) != 1:
                return False
    return True

def f2(a1, a2):
    while a2 != 0:
        a1, a2 = (a2, a1 % a2)
    return a1

def f3(a1):
    if f1(a1):
        return 'pairwise coprime'
    elif f1([a1[0]] + a1[1:]):
        return 'setwise coprime'
    else:
        return 'not coprime'

def f4():
    v1 = [int(x) for v2 in input().split()]
    print(f3(v1))
if __name__ == '__main__':
    f4()
