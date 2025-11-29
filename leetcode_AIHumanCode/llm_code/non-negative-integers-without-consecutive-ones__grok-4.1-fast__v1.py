class Solution:
    def findIntegers(self, num):
        digits = [(num >> i) & 1 for i in range(30, -1, -1)]
        memo = {}
        def dfs(pos, tight, prev):
            if pos == 31:
                return 1
            key = (pos, tight, prev)
            if key in memo:
                return memo[key]
            total = 0
            upper = digits[pos] if tight else 1
            for d in range(upper + 1):
                if d == 1 and prev:
                    continue
                new_tight = 1 if tight and d == upper else 0
                total += dfs(pos + 1, new_tight, d)
            memo[key] = total
            return total
        return dfs(0, 1, 0)
