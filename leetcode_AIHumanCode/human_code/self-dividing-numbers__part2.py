# Time:  O(nlogr) = O(n)
# Space: O(logr) = O(1)
import itertools


class Solution2(object):
    def selfDividingNumbers(self, left, right):
        """
        """
        return [num for num in range(left, right+1) \
                if not any(map(lambda x: int(x) == 0 or num%int(x) != 0, str(num)))]
