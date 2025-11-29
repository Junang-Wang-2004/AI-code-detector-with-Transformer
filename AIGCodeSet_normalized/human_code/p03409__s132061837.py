import sys
import math
from fractions import gcd

def f1(a1, a2):
    return a1 * a2 // gcd(a1, a2)

def f2(a1, a2):
    return math.factorial(a1) // (math.factorial(a1 - a2) * math.factorial(a2))

def f3(a1, a2):
    return math.factorial(a1) // math.factorial(a1 - a2)
v1 = 1000000007
'\n# 標準入力取得\n## 文字列\n =  sys.stdin.readline().rstrip()\n =  list(sys.stdin.readline().rstrip())\n\n## 数値\n =  int(sys.stdin.readline())\n =  map(int, sys.stdin.readline().split())\n =  list(map(int, sys.stdin.readline().split()))\n =  [list(map(int,list(sys.stdin.readline().split()))) for i in range(N)]\n'
v2 = int(sys.stdin.readline())
v3 = [list(map(int, list(sys.stdin.readline().split()))) for v4 in range(v2)]
v5 = [list(map(int, list(sys.stdin.readline().split()))) for v4 in range(v2)]
v3.sort()
v5.sort()
v6 = 0
for v7 in range(v2):
    v8 = -1
    v9 = -1
    for v10 in range(v2):
        if v3[v10][0] < v5[v7][0] and v3[v10][1] < v5[v7][1]:
            if v9 < v3[v10][1]:
                v8 = v10
                v9 = v3[v10][1]
    if v9 > -1:
        v3[v8][0] = 10 ** 10
        v3[v8][1] = 10 ** 10
        v6 += 1
print(v6)
