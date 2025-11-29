# Time:  O(1)
# Space: O(1)

# greedy
class Solution(object):
    def distMoney(self, money, children):
        """
        """
        if money < children*1:
            return -1
        money -= children*1
        q, r = divmod(money, 7)
        return min(q, children) - int(q > children or (q == children and r != 0) or (q == children-1 and r == 3))


