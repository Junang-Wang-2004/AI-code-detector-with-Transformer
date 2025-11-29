def f1():
    v1 = int(input())
    v2 = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
    v3 = [[0, 'a']]
    if v1 == 1:
        print('a')
    else:
        for v4 in range(1, v1):
            v5 = []
            for v6 in v3:
                for v7 in range(v6[0] + 2):
                    v5.append([v7, v6[1] + v2[v7]])
            v3 = v5
            if v4 == v1 - 1:
                for v6 in sorted(v3, key=lambda x: x[1]):
                    print(v6[1])
if __name__ == '__main__':
    f1()
