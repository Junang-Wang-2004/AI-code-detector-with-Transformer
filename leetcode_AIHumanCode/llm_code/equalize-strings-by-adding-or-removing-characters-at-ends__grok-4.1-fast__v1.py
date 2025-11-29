class Solution:
    def minOperations(self, initial, target):
        n, m = len(initial), len(target)
        if n < m:
            initial, target = target, initial
            n, m = m, n
        max_match = 0
        prev = [0] * (m + 1)
        for i in range(1, n + 1):
            curr = [0] * (m + 1)
            for j in range(1, m + 1):
                if initial[i - 1] == target[j - 1]:
                    curr[j] = prev[j - 1] + 1
                    max_match = max(max_match, curr[j])
                # else curr[j] remains 0
            prev = curr
        return n + m - 2 * max_match
