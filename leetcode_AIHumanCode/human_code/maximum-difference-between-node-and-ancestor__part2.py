# Time:  O(n)
# Space: O(h)
# recursive solution
class Solution2(object):
    def maxAncestorDiff(self, root):
        """
        """
        def maxAncestorDiffHelper(node, mx, mn): 
            if not node:
                return 0
            result = max(mx-node.val, node.val-mn)
            mx = max(mx, node.val)
            mn = min(mn, node.val)
            result = max(result, maxAncestorDiffHelper(node.left, mx, mn))
            result = max(result, maxAncestorDiffHelper(node.right, mx, mn))
            return result

        return maxAncestorDiffHelper(root, 0, float("inf"))
