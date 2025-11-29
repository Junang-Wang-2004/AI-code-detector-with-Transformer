def f1():
    v1, v2 = map(int, input().split())
    v3 = [int(input()) for v4 in range(v1)]
    v3.sort()
    v5 = float('inf')
    for v6 in range(v1 - v2 + 1):
        v5 = min(v3[v6 + v2 - 1] - v3[v6], v5)
    print(v5)
if __name__ == '__main__':
    f1()
