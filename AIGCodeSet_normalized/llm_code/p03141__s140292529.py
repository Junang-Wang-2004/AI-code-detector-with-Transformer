def f1():
    v1 = int(input())
    v2 = [[int(x) for v3 in input().split()] for v4 in range(v1)]
    v5 = 0
    for v6 in range(v1):
        v2[v6].append(v2[v6][0] + v2[v6][1])
    v2 = sorted(v2, key=lambda x: -v3[2])
    if v1 == 1:
        print(v2[0][0] - v2[0][1])
    for v6 in range(v1):
        v5 -= v2[v6][1]
    for v6 in range(v1 // 2):
        v5 += v2[2 * v6][0]
    if v1 % 2 == 1:
        v5 += v2[2 * v6 + 1][0]
    print(v5)
if __name__ == '__main__':
    f1()
