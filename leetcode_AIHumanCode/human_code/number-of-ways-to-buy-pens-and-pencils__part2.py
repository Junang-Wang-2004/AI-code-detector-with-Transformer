# Time:  O(t / c1), c1 = max(cost1, cost2)
#                 , c2 = min(cost1, cost2)
# Space: O(1)
# math
class Solution2(object):
    def waysToBuyPensPencils(self, total, cost1, cost2):
        """
        """
        if cost1 < cost2:
            cost1, cost2 = cost2, cost1
        return sum((total-i*cost1)//cost2+1 for i in range(total//cost1+1))
