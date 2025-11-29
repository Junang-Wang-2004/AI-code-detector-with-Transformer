"""
D - We Like AGC
https://atcoder.jp/contests/abc122/tasks/abc122_d

"""
import sys
import re
v1 = None
v2 = None

def f1(a1):
    if re.search('AGC|GAC|ACG|A.GC|AG.C', a1):
        return False
    return True

def f2(a1, a2):
    global memo
    if a2 in v2[a1]:
        return v2[a1][a2]
    if a1 == v1:
        return 1
    v1 = 0
    for v2 in 'ACGT':
        if f1(a2 + v2):
            v1 = (v1 + f2(a1 + 1, a2[1:] + v2)) % (10 ** 9 + 7)
    v2[a1][a2] = v1
    return v1

def f3(a1):
    global N, memo
    v1 = int(input())
    v2 = [dict() for v3 in range(v1 + 1)]
    v4 = f2(0, 'TTT')
    print(v4)
if __name__ == '__main__':
    f3(sys.argv[1:])
