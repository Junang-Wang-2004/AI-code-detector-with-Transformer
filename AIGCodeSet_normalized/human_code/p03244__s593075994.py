from collections import Counter

def f1():
    return map(int, input().split())

def f2():
    return int(input())

def f3():
    v1 = f2()
    v2 = list(f1())
    v3 = [v2[i] for v4 in range(v1) if v4 % 2 == 0]
    v5 = [v2[v4] for v4 in range(v1) if v4 % 2 == 1]
    v6 = Counter(v3)
    v7 = Counter(v5)
    if v6.most_common()[0][0] == v7.most_common()[0][0]:
        if len(v6.most_common()) > 1 and len(v7.most_common()) > 1:
            if v6.most_common()[1][1] > v7.most_common()[1][1]:
                v8 = v6.most_common()[1][1]
                v9 = v6.most_common()[0][1]
            else:
                v8 = v6.most_common()[0][1]
                v9 = v7.most_common()[1][1]
        else:
            v8 = v6.most_common()[0][1]
            v9 = 0
    else:
        v8 = v6.most_common()[0][1]
        v9 = v7.most_common()[0][1]
    print(v1 - v8 - v9)
if __name__ == '__main__':
    f3()
