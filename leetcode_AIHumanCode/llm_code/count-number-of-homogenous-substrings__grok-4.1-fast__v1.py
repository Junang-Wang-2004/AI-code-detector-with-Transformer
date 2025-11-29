class Solution:
    def countHomogenous(self, s):
        MOD = 1000000007
        total = 0
        curr = None
        streak = 0
        for ch in s:
            if ch == curr:
                streak += 1
            else:
                if curr is not None:
                    total = (total + streak * (streak + 1) // 2) % MOD
                curr = ch
                streak = 1
        if curr is not None:
            total = (total + streak * (streak + 1) // 2) % MOD
        return total
