class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rangeSumBST(self, root, L, R):
        def helper(curr):
            if not curr:
                return 0
            ans = 0
            if L <= curr.val <= R:
                ans += curr.val
            if L < curr.val:
                ans += helper(curr.left)
            if curr.val < R:
                ans += helper(curr.right)
            return ans
        return helper(root)
