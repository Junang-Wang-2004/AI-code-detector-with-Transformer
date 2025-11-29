class Solution:
    def countArrangement(self, n):
        used = [False] * (n + 1)
        
        def backtrack(pos):
            if pos > n:
                return 1
            res = 0
            for val in range(1, n + 1):
                if not used[val] and (val % pos == 0 or pos % val == 0):
                    used[val] = True
                    res += backtrack(pos + 1)
                    used[val] = False
            return res
        
        return backtrack(1)
