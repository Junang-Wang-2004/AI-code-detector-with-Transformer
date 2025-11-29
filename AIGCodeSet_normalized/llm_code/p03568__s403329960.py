import itertools

def f1():
    v1 = int(input())
    v2 = list(map(int, input().split(' ')))
    v3 = [[] for v4 in range(v1)]
    for v5 in range(v1):
        v3[v5].append(v2[v5] - 1)
        v3[v5].append(v2[v5])
        v3[v5].append(v2[v5] + 1)
    v6 = 0
    for v7 in list(itertools.product(*v3)):
        if all((abs(v7[v5] - v2[v5]) <= 1 for v5 in range(v1))):
            if all((x % 2 == 0 for v8 in v7)):
                v6 += 1
    print(v6)
f1()
