class Solution(object):
    def findKthSmallest(self, coins, k):
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        n = len(coins)
        min_coin = min(coins)
        multiples = []
        for mask in range(1, 1 << n):
            clcm = 1
            bits = 0
            for j in range(n):
                if mask & (1 << j):
                    clcm = clcm * coins[j] // gcd(clcm, coins[j])
                    bits += 1
            sg = 1 if bits % 2 == 1 else -1
            multiples.append((clcm, sg))

        def feasible(val):
            cnt = 0
            for d, s in multiples:
                cnt += s * (val // d)
            return cnt >= k

        left, right = min_coin, k * min_coin
        while left < right:
            pivot = (left + right) // 2
            if feasible(pivot):
                right = pivot
            else:
                left = pivot + 1
        return left
