# Time:  O(n)
# Space: O(n), this doesn't satisfy the question
from collections import Counter
class Solution3(object):
    def findDuplicates(self, nums):
        """
        """
        return [elem for elem, count in list(Counter(nums).items()) if count == 2]

