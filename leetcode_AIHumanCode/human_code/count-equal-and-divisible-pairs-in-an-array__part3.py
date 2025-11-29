# Time:  O(n^2)
# Space: O(n)
import collections


# brute force
class Solution3(object):
    def countPairs(self, nums, k):
        """
        """
        idxs = collections.defaultdict(list)
        for i, x in enumerate(nums):
            idxs[x].append(i)
        return sum(idx[i]*idx[j]%k == 0 for idx in idxs.values() for i in range(len(idx)) for j in range(i+1, len(idx)))
