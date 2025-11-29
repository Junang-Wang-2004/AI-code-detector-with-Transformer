import sys
sys.setrecursionlimit(10 ** 7)
from pprint import pprint as pp
from pprint import pformat as pf
import math
import bisect

class C1:

    def __init__(self, a1, a2):
        self.n = a1
        self.a_s = a2
        self.extra = 1 if self.n % 2 == 0 else 2
        self.dp = self.prepare_dp()

    def prepare_dp(self):
        v1 = [None] * (self.n + 1)
        for v2, v3 in enumerate(v1):
            v1[v2] = [-1 * math.inf] * (1 + self.extra)
        v1[0][0] = 0
        return v1

    def run(self):
        v1 = 1 + self.n % 2
        for v2, v3 in enumerate(self.a_s):
            for v4 in range(self.extra):
                self.dp[v2 + 1][v4 + 1] = self.dp[v2][v4]
            for v4 in range(self.extra + 1):
                v5 = self.dp[v2][v4]
                if (v2 + v4) % 2 == 0:
                    v5 += v3
                self.dp[v2 + 1][v4] = max(self.dp[v2 + 1][v4], v5)
        return self.dp[n][v1]
if __name__ == '__main__':
    v1 = int(input())
    v2 = list(map(int, input().split()))
    v3 = C1(v1, v2).run()
    print(v3)
