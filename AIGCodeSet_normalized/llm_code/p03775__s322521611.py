import sys

def f1(a1):
    v1 = []
    v2 = a1
    for v3 in range(2, int(-(-a1 ** 0.5 // 1)) + 1):
        if v2 % v3 == 0:
            v4 = 0
            while v2 % v3 == 0:
                v4 += 1
                v2 //= v3
            v1.append([v3, v4])
    if v2 != 1:
        v1.append([v2, 1])
    if v1 == []:
        v1.append([a1, 1])
    return v1

def f2():
    v1 = int(input())
    if v1 == 1 or v1 == 2:
        print(1)
        sys.exit()
    list = f1(v1)
    list.sort(reverse=True)
    v2 = 1
    v3 = 1
    for v4 in range(len(list)):
        for v5 in range(list[v4][1]):
            if v2 <= v3:
                v2 *= list[v4][0]
            else:
                v3 *= list[v4][0]
    v6 = max(len(str(v2)), len(str(v3)))
    print(v6)
if __name__ == '__main__':
    f2()
