# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# iterative stack solution
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        """
        result = 0
        stack = [(root, 0, float("inf"))]
        while stack:
            node, mx, mn = stack.pop()
            if not node:
                continue
            result = max(result, mx-node.val, node.val-mn)
            mx = max(mx, node.val)
            mn = min(mn, node.val)
            stack.append((node.left, mx, mn))
            stack.append((node.right, mx, mn))
        return result


