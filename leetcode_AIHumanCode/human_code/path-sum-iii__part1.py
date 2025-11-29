# Time:  O(n)
# Space: O(h)

import collections


class Solution(object):
    def pathSum(self, root, sum):
        """
        """
        def pathSumHelper(root, curr, sum, lookup):
            if root is None:
                return 0
            curr += root.val
            result = lookup[curr-sum] if curr-sum in lookup else 0
            lookup[curr] += 1
            result += pathSumHelper(root.left, curr, sum, lookup) + \
                      pathSumHelper(root.right, curr, sum, lookup)
            lookup[curr] -= 1
            if lookup[curr] == 0:
                del lookup[curr]
            return result

        lookup = collections.defaultdict(int)
        lookup[0] = 1
        return pathSumHelper(root, 0, sum, lookup)


