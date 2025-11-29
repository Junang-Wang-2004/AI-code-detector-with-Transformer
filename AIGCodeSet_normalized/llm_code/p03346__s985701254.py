import sys
if __name__ == '__main__':
    v1 = int(input())
    v2 = []
    v3 = [0] * (v1 + 1)
    for v4 in range(1, v1 + 1):
        v5 = int(input())
        v3[v5] = v4
    v6 = 1
    v7 = 1
    for v4 in range(1, v1):
        if v3[v4] < v3[v4 + 1]:
            v6 += 1
            v7 = max(v6, v7)
        else:
            v6 = 1
    print(v1 - v7)
