def f1():
    v1, v2, v3 = [int(x) for v4 in input().split()]
    sum = v1 + v2 + v3
    max = v1
    if max <= v2:
        max = v2
    if max <= v3:
        max = v3
    if max * 2 == sum:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    f1()
