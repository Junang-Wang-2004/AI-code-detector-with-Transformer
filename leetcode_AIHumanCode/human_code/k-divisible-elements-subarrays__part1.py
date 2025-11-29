# Time:  O(n^2)
# Space: O(t), t is the size of trie

import collections


# trie
class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        """
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        result = 0
        for i in range(len(nums)):
            cnt = 0
            curr = trie
            for j in range(i, len(nums)):
                cnt += (nums[j]%p == 0)
                if cnt > k:
                    break
                if nums[j] not in curr:
                    result += 1
                curr = curr[nums[j]]
        return result


