class Solution:
    def minTime(self, s, order, k):
        n = len(s)
        burden = n * (n + 1) // 2
        if burden < k:
            return -1
        m = len(order)
        prior = [-1] + list(range(n - 1))
        after = list(range(1, n + 1))
        count = 0
        while count < m:
            spot = order[m - 1 - count]
            lp = prior[spot]
            rp = after[spot]
            deduct = (spot - lp) * (rp - spot)
            burden -= deduct
            if burden < k:
                return m - 1 - count
            if lp >= 0:
                after[lp] = rp
            if rp < n:
                prior[rp] = lp
            count += 1
        return 0
