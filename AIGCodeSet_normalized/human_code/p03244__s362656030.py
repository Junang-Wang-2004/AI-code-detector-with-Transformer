import collections

def f1(a1, a2, a3, a4):
    v1 = a4 - a2
    for v2, v3 in [b for v4 in a3 if v4[1] > v1]:
        if a1 != v2:
            return a2 + v3
    return a4

def f2(a1, a2):
    v1 = -1
    v2 = a2[0][1]
    for v3, v4 in a1:
        if v4 <= v1 - v2:
            break
        v1 = f1(v3, v4, a2, v1)
    return v1

def f3():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    v3 = v2[::2]
    v4 = v2[1::2]
    v5 = collections.Counter(v3)
    v6 = collections.Counter(v4)
    v7 = v5.most_common()
    v8 = v6.most_common()
    if len(v7) == 1 and len(v8) == 1 and (v7[0][0] == v8[0][0]):
        print(v1 // 2)
        return
    print(v1 - f2(v7, v8))
if __name__ == '__main__':
    f3()
