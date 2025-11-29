MOD = 10**9 + 7

class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        n = len(s)
        m = len(t)
        if k == 0:
            return 1 if m == 0 else 0
        trans = [[0, 1], [n - 1, n -
