class Solution:
    def houseOfCards(self, n):
        counts = [0] * (n + 1)
        counts[0] = 1
        max_base = (n + 1) // 3
        for base in range(1, max_base + 1):
            cost = 3 * base - 1
            if cost > n:
                continue
            temp = [0] * (n + 1)
            for total in range(cost, n + 1):
                temp[total] = counts[total - cost]
            for total in range(cost, n + 1):
                counts[total] += temp[total]
        return counts[n]
