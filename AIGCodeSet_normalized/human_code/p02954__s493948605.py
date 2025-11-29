"""
Created on Sat Apr 20 20:47:47 2019

@author: Owner
"""
import numpy as np
import sys
import collections
import scipy.misc
import math
from operator import itemgetter
import itertools
import copy
import bisect
import heapq
from collections import deque

def f1(a1):
    v1 = 2
    v2 = []
    while v1 * v1 <= a1:
        while a1 % v1 == 0:
            a1 /= v1
            v2.append(int(v1))
        v1 += 1
    if a1 > 1:
        v2.append(int(a1))
    return v2

def f2(a1):
    if a1 > 0:
        return f2(a1 // 10) + [a1 % 10]
    else:
        return []

def f3(a1, a2):
    """
    概要: リストからある値に最も近い値のインデックスを取得する関数
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    """
    v1 = np.abs(np.asarray(a1) - a2).argmin()
    return v1

def f4(a1, a2, a3=False):
    if a2 in a1:
        return a1.index(a2)
    else:
        return a3

class C1(object):

    def __init__(self, a1=1):
        self.par = [i for v1 in range(a1)]
        self.rank = [0 for v2 in range(a1)]
        self.size = [1 for v2 in range(a1)]

    def find(self, a1):
        """
        x が属するグループを探索
        """
        if self.par[a1] == a1:
            return a1
        else:
            self.par[a1] = self.find(self.par[a1])
            return self.par[a1]

    def union(self, a1, a2):
        """
        x と y のグループを結合
        """
        a1 = self.find(a1)
        a2 = self.find(a2)
        if a1 != a2:
            if self.rank[a1] < self.rank[a2]:
                a1, a2 = (a2, a1)
            if self.rank[a1] == self.rank[a2]:
                self.rank[a1] += 1
            self.par[a2] = a1
            self.size[a1] += self.size[a2]

    def is_same(self, a1, a2):
        """
        x と y が同じグループか否か
        """
        return self.find(a1) == self.find(a2)

    def get_size(self, a1):
        """
        x が属するグループの要素数
        """
        a1 = self.find(a1)
        return self.size[a1]
"\nN, X = map(int, input().split())\n\nx = list(map(int, input().split()))\n\nP = [0]*N\nY = [0]*N\nfor n in range(N):\n    P[n], Y[n] = map(int, input().split())\n\n# 多次元配列の宣言（あとでintにすること。）（タプルにすること。）\ndp = np.zeros((N+1, 4,4,4))\n    \nall(nstr.count(c) for c in '753')\n\n# 複数配列を並び替え\nABT = zip(A, B, totAB)\nresult = 0\n# itemgetterには何番目の配列をキーにしたいか渡します\nsorted(ABT,key=itemgetter(2))\nA, B, totAB = zip(*ABT)\nA.sort(reverse=True)\n\n# 2進数のbit判定\n(x >> i) & 1\n\n# dp最小化問題\ndp = [np.inf]*N\nfor n in range(N):\n    if n == 0:\n        dp[n] = 0\n    else:\n        for k in range(1,K+1):\n            if n-k >= 0:\n                dp[n] = min(dp[n], dp[n-k] + abs(h[n]-h[n-k]))\n            else:\n                break\n# 累積和\nadd = 1 # 問題によって決まる\nres = 0\nsums = [0]*(len(nums)+1)\nfor i in range(len(nums)):\n    sums[i+1] = sums[i] + nums[i]\nfor i in range(0, len(nums), 2):\n    left = i\n    right = min(i+add, len(nums))\n    tmp = sums[right] - sums[left]\n    res = max(tmp, res)\n\n#２分探索\nli, ri = bisect.bisect_left(p_ac, l[i]-1), bisect.bisect_right(p_ac, r[i]-1)    \n\n#ソート関数\norg_list = [3, 1, 4, 5, 2]\nnew_list = sorted(org_list)\nprint(org_list)\nprint(new_list)\n# [3, 1, 4, 5, 2]\n# [1, 2, 3, 4, 5]\n\n#Distance Transformation\n    for h in range(0,H):\n        for w in range(0,W):\n            if h == 0 and w == 0:\n                pass\n            elif h == 0:\n                D[H-h-1][W-w-1]= min(D[H-h-1][W-w-1], D[H-h-1][W-w]+1)\n            elif w == 0:   \n                D[H-h-1][W-w-1]= min(D[H-h-1][W-w-1], D[H-h][W-w-1]+1)\n            else:\n                D[H-h-1][W-w-1]= min(D[H-h-1][W-w-1], D[H-h][W-w-1]+1, D[H-h-1][W-w]+1, D[H-h][W-w]+2)\n            d_max = max(D[H-h-1][W-w-1], d_max)\n\n"
v1 = input()

def f9():
    v1 = len(v1)
    v2 = 0
    v3 = v1 - 1
    v4 = 'R'
    v5 = [n for v6 in range(v1) if v1[v6] == 'R']
    v7 = [v6 for v6 in range(v1) if v1[v6] == 'L']
    v8 = v1
    v9 = [0] * v1
    for v6 in range(v1):
        if v8 == v1:
            v3 = v1.find('L')
            v8 = v3
            if v8 % 2 == 0:
                v9[v3] += 1
            else:
                v9[v3 - 1] += 1
            v8 -= 1
            continue
        if v1[v6] == 'R':
            if v1[v6] != v1[v6 - 1]:
                v10 = bisect.bisect_left(v7, v6)
                if v7[v10] < v6:
                    v3 = v7[v10 + 1]
                else:
                    v3 = v7[v10]
                v8 = v3 - v6
                if v8 % 2 == 0:
                    v9[v3] += 1
                else:
                    v9[v3 - 1] += 1
                v8 -= 1
                continue
            else:
                if v8 % 2 == 0:
                    v9[v3] += 1
                else:
                    v9[v3 - 1] += 1
                v8 -= 1
                continue
        if v1[v6] == 'L':
            if v1[v6] == v1[v6 - 1]:
                if v8 % 2 == 0:
                    v9[v3] += 1
                else:
                    v9[v3 - 1] += 1
                v8 += 1
                continue
            else:
                v3 = v6
                v8 = 0
                if v8 % 2 == 0:
                    v9[v3] += 1
                else:
                    v9[v3 - 1] += 1
                v8 += 1
                continue
    print(*v9, sep=' ')
if __name__ == '__main__':
    f9()
