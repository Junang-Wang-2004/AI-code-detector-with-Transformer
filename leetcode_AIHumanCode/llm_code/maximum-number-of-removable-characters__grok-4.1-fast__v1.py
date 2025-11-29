class Solution:
    def maximumRemovals(self, s, p, removable):
        n = len(s)
        m = len(removable)
        rem_cost = [m + 1] * n
        for idx in range(m):
            rem_cost[removable[idx]] = idx + 1
        
        def feasible(k):
            p_idx = 0
            p_len = len(p)
            for i in range(n):
                if rem_cost[i] > k and s[i] == p[p_idx]:
                    p_idx += 1
                    if p_idx == p_len:
                        return True
            return False
        
        l, r = 0, m
        while l <= r:
            mid = (l + r) // 2
            if feasible(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r
