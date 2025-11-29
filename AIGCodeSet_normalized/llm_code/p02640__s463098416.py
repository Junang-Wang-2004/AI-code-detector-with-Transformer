v1 = list(map(int, input().split()))

def f1(a1):
    for v1 in range(a1[0] + 1):
        for v2 in range(a1[0] + 1):
            if v1 + v2 == a1[0] and v1 * 2 + v2 * 4 == a1[1]:
                print('Yes')
                return
    print('No')
    return
f1(v1)
