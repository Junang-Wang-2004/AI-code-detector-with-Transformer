# Time:  O(n^2)
# Space: O(h)
class Solution2(object):
    def pathSum(self, root, sum):
        """
        """
        def pathSumHelper(root, prev, sum):
            if root is None:
                return 0

            curr = prev + root.val
            return int(curr == sum) + \
                   pathSumHelper(root.left, curr, sum) + \
                   pathSumHelper(root.right, curr, sum)

        if root is None:
            return 0

        return pathSumHelper(root, 0, sum) + \
               self.pathSum(root.left, sum) + \
               self.pathSum(root.right, sum)

