def f1(a1):
    v1 = len(a1)
    for v2 in range(v1 - 1):
        if a1[v2] % 2 != 0 and a1[v2 + 1] % 2 != 0:
            return False
    return True

def f2():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    if f1(v2):
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    f2()
