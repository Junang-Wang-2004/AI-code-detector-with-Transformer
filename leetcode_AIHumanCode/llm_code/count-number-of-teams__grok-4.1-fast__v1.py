class Solution:
    def numTeams(self, rating):
        n = len(rating)
        total = 0
        for m in range(n):
            lt_smaller = 0
            lt_larger = 0
            for l in range(m):
                if rating[l] < rating[m]:
                    lt_smaller += 1
                else:
                    lt_larger += 1
            rt_smaller = 0
            rt_larger = 0
            for r in range(m + 1, n):
                if rating[r] < rating[m]:
                    rt_smaller += 1
                else:
                    rt_larger += 1
            total += lt_smaller * rt_larger + lt_larger * rt_smaller
        return total
