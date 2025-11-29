from collections import deque

def f1():
    v1 = int(input())
    v2 = deque(sorted((int(input()) for v3 in range(v1))))
    v4 = deque()
    v4.append(v2.popleft())
    v5 = 0
    for v6 in range(v1 - 1):
        v7 = v2[0]
        v8 = v2[-1]
        v9 = v4[0]
        v10 = v4[-1]
        v11 = abs(v7 - v9)
        v12 = abs(v7 - v10)
        v13 = abs(v8 - v9)
        v14 = abs(v8 - v10)
        v15 = [v11, v12, v13, v14]
        v16 = v15.index(max(v15))
        if v16 == 0:
            v5 += v11
            v4.appendleft(v2.popleft())
        elif v16 == 1:
            v5 += v12
            v4.append(v2.popleft())
        elif v16 == 2:
            v5 += v13
            v4.appendleft(v2.pop())
        else:
            v5 += v14
            v4.append(v2.pop())
    print(v5)
if __name__ == '__main__':
    f1()
