# Time:  O(nlogn)
# Space: O(n)
import itertools
import bisect


class BIT(object):  # 0-indexed.
    def __init__(self, n):
        self.__bit = [0]*(n+1)  # Extra one for dummy node.

    def add(self, i, val):
        i += 1  # Extra one for dummy node.
        while i < len(self.__bit):
            self.__bit[i] += val
            i += (i & -i)

    def query(self, i):
        i += 1  # Extra one for dummy node.
        ret = 0
        while i > 0:
            ret += self.__bit[i]
            i -= (i & -i)
        return ret


# bit, fenwick tree, coordinate compression
class Solution2(object):
    def numberOfPairs(self, nums1, nums2, diff):
        """
        """
        sorted_nums = sorted(set(x-y for x, y in zip(nums1, nums2)))
        num_to_idx = {x:i for i, x in enumerate(sorted_nums)}
        result = 0
        bit = BIT(len(num_to_idx))
        for x, y in zip(nums1, nums2):
            result += bit.query(bisect.bisect_right(sorted_nums, (x-y)+diff)-1)
            bit.add(num_to_idx[x-y], 1)
        return result


