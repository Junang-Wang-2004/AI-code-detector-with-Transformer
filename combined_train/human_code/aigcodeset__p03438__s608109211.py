import sys
v1 = sys.stdin.buffer.read
v2 = sys.stdin.buffer.readline
v3 = lambda: int(v2())
v4 = lambda: map(int, v2().split())
v5 = lambda: list(map(int, v2().split()))
v6 = lambda: map(int, v1().split())
v7 = lambda: v2().rstrip().decode('utf-8')

def f1():
    v1 = v3()
    v2 = v5()
    v3 = v5()
    v4 = sum(v3) - sum(v2)
    v5, v6 = (0, 0)
    for v7 in range(v1):
        if v2[v7] == v3[v7]:
            continue
        elif v2[v7] > v3[v7]:
            v6 += v2[v7] - v3[v7]
        else:
            v8 = v3[v7] - v2[v7]
            if v8 % 2 == 0:
                v5 += v8 // 2
            else:
                v5 += v8 // 2 + 1
                v6 += 1
    if v4 < 0:
        v9 = 'No'
    elif v4 < v5 or v4 < v6:
        v9 = 'No'
    elif v6 + 2 * (v4 - v5) == v4:
        v9 = 'Yes'
    else:
        v9 = 'No'
    print(v9)
if __name__ == '__main__':
    f1()
