class Solution:
    def maxProfit(self, prices, profits):
        INF = float('-inf')
        if len(prices) < 3:
            return -1
        
        uniq = sorted(set(prices))
        pos = {val: i for i, val in enumerate(uniq)}
        sz = len(uniq)
        
        class MaxFenwick:
            def __init__(self, n):
                self.n = n
                self.data = [INF] * (n + 2)
            
            def modify(self, i, v):
                i += 1
                while i <= self.n:
                    self.data[i] = max(self.data[i], v)
                    i += i & -i
            
            def prefix_max(self, i):
                if i < 0:
                    return INF
                i += 1
                mx = INF
                while i > 0:
                    mx = max(mx, self.data[i])
                    i -= i & -i
                return mx
        
        first = MaxFenwick(sz)
        second = MaxFenwick(sz)
        best = INF
        
        for i in range(len(prices)):
            p = prices[i]
            g = profits[i]
            rk = pos[p]
            
            prior_second = second.prefix_max(rk - 1)
            best = max(best, prior_second + g)
            
            prior_first = first.prefix_max(rk - 1)
            first.modify(rk, g)
            
            second.modify(rk, prior_first + g)
        
        return best if best != INF else -1
