# Time:  O(n), n is 10^3
# Space: O(1)
import collections
from functools import reduce


class Solution2(object):
    def findEvenNumbers(self, digits):
        """
        """
        result, cnt = [], collections.Counter(digits)
        for i in range(1, 10):
            for j in range(10):
                for k in range(0, 10, 2):
                    if cnt[i] > 0 and cnt[j] > (j == i) and cnt[k] > (k == i) + (k == j):
                        result.append(i*100 + j*10 + k)
        return result


