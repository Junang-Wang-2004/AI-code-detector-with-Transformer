class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        cost_a = 0
        cost_b = 0
        for i in range(n):
            expected_a = i % 2
            expected_b = 1 ^ (i % 2)
            if int(s[i]) != expected_a:
                cost_a += 1
            if int(s[i]) != expected_b:
                cost_b += 1
        return min(cost_a, cost_b)
