class Solution:
    def reinitializePermutation(self, n):
        m = n - 1
        tgt = 1 % m
        steps = 1
        pos = 2 % m
        while pos != tgt:
            pos = (pos * 2) % m
            steps += 1
        return steps
