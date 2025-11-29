class Solution(object):
    def miceAndCheese(self, reward1, reward2, k):
        base = sum(reward2)
        gains = sorted(r1 - r2 for r1, r2 in zip(reward1, reward2), reverse=True)
        return base + sum(gains[:k])
