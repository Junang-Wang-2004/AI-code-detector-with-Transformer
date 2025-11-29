from collections import defaultdict

def f1():
    v1, v2 = map(int, input().split())
    v3 = list(map(int, input().split()))
    v4 = [0] * v1
    v5 = defaultdict(int)
    v5[0] = 1
    v6 = 0
    v7 = 0
    if v2 == 1:
        print(sum(list(map(lambda x: x % 2, v3))))
        return
    for v8 in range(v1):
        if v8 >= v2 - 1:
            v5[v4[v8 - (v2 - 1)]] -= 1
        v6 = (v6 + v3[v8]) % v2
        v4[v8] = v6
        v7 += v5[v6]
        v5[v6] += 1
    print(v7)
if __name__ == '__main__':
    f1()
