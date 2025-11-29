class Solution(object):
    def maximumBeauty(self, items, queries):
        products = sorted(items)
        prefix_max = []
        cur_max = 0
        for price, beauty in products:
            cur_max = max(cur_max, beauty)
            prefix_max.append(cur_max)
        
        prices = [p[0] for p in products]
        n = len(prices)
        
        def last_leq(target):
            l, r = 0, n - 1
            pos = -1
            while l <= r:
                m = l + (r - l) // 2
                if prices[m] <= target:
                    pos = m
                    l = m + 1
                else:
                    r = m - 1
            return pos
        
        ans = []
        for q in queries:
            idx = last_leq(q)
            ans.append(prefix_max[idx] if idx >= 0 else 0)
        return ans
