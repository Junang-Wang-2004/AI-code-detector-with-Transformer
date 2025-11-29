import sys
v1 = sys.stdin.readline
from bisect import bisect_left, insort_left

def f1():
    v1 = int(v1())
    v2 = list(v1().rstrip())
    v3 = int(v1())
    v4 = [[] for v5 in range(26)]
    for v5, v6 in enumerate(v2):
        v7 = ord(v6) - 97
        v4[v7].append(v5)
    v8 = []
    for v9 in range(v3):
        v10, v5, v11 = v1().rstrip().split()
        v5 = int(v5) - 1
        if v10 == '1':
            if v2[v5] == v11:
                continue
            v12 = ord(v2[v5]) - 97
            v13 = v4[v12]
            v14 = ord(v11) - 97
            v13.pop(bisect_left(v13, v5))
            v2[v5] = v11
            insort_left(v4[v14], v5)
        else:
            v11 = int(v11) - 1
            v15 = 0
            for v16 in v4:
                v17 = len(v16)
                v18 = bisect_left(v16, v5, 0, v17)
                if v18 == v17:
                    continue
                if v5 <= v16[v18] <= v11:
                    v15 += 1
            v8.append(v15)
    print(*v8, sep='\n')
if __name__ == '__main__':
    f1()
