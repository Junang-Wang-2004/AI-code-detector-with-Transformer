# Time:  O(n)
# Space: O(1)
# one-liner solution
class Solution2(object):
    def average(self, salary):
        """
        """
        return 1.0*(sum(salary)-min(salary)-max(salary))/(len(salary)-2)
