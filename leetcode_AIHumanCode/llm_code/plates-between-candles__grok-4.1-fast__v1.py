class Solution:
    def platesBetweenCandles(self, s, queries):
        n = len(s)
        prev_candle = [-1] * n
        pos = -1
        for i in range(n):
            if s[i] == '|':
                pos = i
            prev_candle[i] = pos
        next_candle = [n] * n
        pos = n
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                pos = i
            next_candle[i] = pos
        stars = [0] * (n + 1)
        for i in range(n):
            stars[i + 1] = stars[i] + (s[i] == '*')
        ans = []
        for L, R in queries:
            leftmost = next_candle[L]
            if leftmost > R:
                ans.append(0)
                continue
            rightmost = prev_candle[R]
            if rightmost < leftmost:
                ans.append(0)
                continue
            ans.append(stars[rightmost] - stars[leftmost + 1])
        return ans
