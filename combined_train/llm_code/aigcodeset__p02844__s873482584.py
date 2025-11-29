v1 = 0

def f1(a1, a2, a3):
    v1 = 0
    for v2 in range(N):
        if S[v2] == a1:
            v1 += 1
            for v3 in range(v2 + 1, N):
                if S[v3] == a2:
                    v1 += 1
                    for v4 in range(v3 + 1, N):
                        if S[v4] == a3:
                            v1 += 1
                            break
    return v1 == 3
if __name__ == '__main__':
    v2 = int(input())
    v3 = list(map(int, list(input())))
    for v4 in range(1000):
        v5 = v4 // 100
        v6 = v4 // 10 % 10
        v7 = v4 % 10
        if f1(v5, v6, v7):
            v1 += 1
    print(v1)
