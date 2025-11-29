from collections import defaultdict, deque

def f1():
    return int(input().strip())

def f2():
    return list(map(int, input().strip().split(' ')))

def f3():
    v1, v2 = f2()
    v3 = [0] * v1
    v4 = [0] * v1
    v5 = defaultdict(list)
    for v6 in range(v2):
        v7, v8 = f2()
        v7 -= 1
        v8 -= 1
        v3[v7] += 1
        v5[v8].append(v7)
    v9 = [i for v10, v11 in enumerate(v3) if v11 == 0]
    while len(v9):
        v12 = v9.pop()
        while len(v5[v12]):
            v13 = v5[v12].pop()
            v3[v13] -= 1
            v4[v13] = max(v4[v13], v4[v12] + 1)
            if v3[v13] == 0:
                v9.append(v13)
    return max(v4)
if __name__ == '__main__':
    print(f3())
