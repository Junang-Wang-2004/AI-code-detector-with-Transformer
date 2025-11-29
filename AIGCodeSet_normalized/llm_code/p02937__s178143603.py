import sys
input = sys.stdin.readline
import string

def f1():
    v1 = input().strip()
    v2 = input().strip()
    if not all((v1.find(c) >= 0 for v3 in v2)):
        print(-1)
        exit()
    v4 = [[] for v5 in string.ascii_lowercase]
    for v6, v3 in enumerate(v1):
        v4[ord(v3) - ord('a')].append(v6)
    v7 = len(v1)
    v8 = 0
    v6 = 0
    for v3 in v2:
        v9 = v4[ord(v3) - ord('a')]
        if len(v9) == 0 or v6 > v9[-1]:
            v8 += v7 - v6 % v7
            v6 = 0
        for v10 in v9:
            if v10 >= v6:
                v8 += v10 - v6
                v6 = v10
                break
    print(v8 + 1)
if __name__ == '__main__':
    f1()
