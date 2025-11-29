def f1():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    return (v1, v2)

def f2():
    v1, v2 = f1()
    v3 = sum([1 for v4 in v2 if v4 % 4 == 0])
    v5 = sum([1 for v4 in v2 if v4 % 4 != 0 and v4 % 2 == 0])
    if v1 // 2 <= v3:
        print('Yes')
        return
    v1 -= 2 * v3
    if v1 <= v5:
        print('Yes')
        return
    print('No')
if __name__ == '__main__':
    f2()
