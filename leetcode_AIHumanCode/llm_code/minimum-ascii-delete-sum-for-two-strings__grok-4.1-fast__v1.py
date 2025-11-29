class Solution:
    def minimumDeleteSum(self, s1, s2):
        m, n = len(s1), len(s2)
        total_cost = sum(ord(c) for c in s1 + s2)
        prev = [0] * (n + 1)
        for i in range(m):
            curr = [0] * (n + 1)
            for j in range(n):
                if s1[i] == s2[j]:
                    curr[j + 1] = prev[j] + ord(s1[i])
                else:
                    curr[j + 1] = max(prev[j + 1], curr[j])
            prev = curr
        return total_cost - 2 * prev[n]
