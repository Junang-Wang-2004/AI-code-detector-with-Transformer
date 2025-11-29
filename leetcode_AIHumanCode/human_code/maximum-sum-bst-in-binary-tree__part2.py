# Time:  O(n)
# Space: O(h)
# dfs solution with recursion
class Solution2(object):
    def maxSumBST(self, root):
        """
        """
        def dfs(node, result):
            if not node:
                return True, 0, float("inf"), float("-inf")
            lvalid, lsum, lmin, lmax = dfs(node.left, result)
            rvalid, rsum, rmin, rmax = dfs(node.right, result)
            if lvalid and rvalid and lmax < node.val < rmin:
                total = lsum + node.val + rsum
                result[0] = max(result[0], total)
                return True, total, min(lmin, node.val), max(node.val, rmax)
            return False, 0, 0, 0

        result = [0]
        dfs(root, result)
        return result[0]
