class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        counts = [[0] * 10 for _ in range(10)]
        for i in range(n):
            dig = int(s[i])
            new_counts = [[0] * 10 for _ in range(10)]
            for m in range(1, 10):
                new_counts[m][dig % m] += 1
                for r in range(m):
                    nr = (r * 10 + dig) % m
                    new_counts[m][nr] += counts[m][r]
            counts = new_counts
            ans += counts[dig][0]
        return ans
