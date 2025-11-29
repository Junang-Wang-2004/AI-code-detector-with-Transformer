class Solution:
    def stoneGameIX(self, stones):
        cnt = [0] * 3
        for val in stones:
            cnt[val % 3] += 1
        a, b, c = cnt
        if a % 2 == 0:
            return b > 0 and c > 0
        return abs(b - c) >= 3
