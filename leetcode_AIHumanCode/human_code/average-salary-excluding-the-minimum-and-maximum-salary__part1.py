# Time:  O(n)
# Space: O(1)

# one pass solution
class Solution(object):
    def average(self, salary):
        """
        """
        total, mi, ma = 0, float("inf"), float("-inf")
        for s in salary:
            total += s
            mi, ma = min(mi, s), max(ma, s)
        return 1.0*(total-mi-ma)/(len(salary)-2)


