# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        def traverse(curr: TreeNode, parity: int) -> int:
            if not curr:
                return 0
            parity ^= 1 << (curr.val - 1)
            if not curr.left and not curr.right:
                return 1 if (parity & (parity - 1)) == 0 else 0
            paths = 0
            if curr.left:
                paths += traverse(curr.left, parity)
            if curr.right:
                paths += traverse(curr.right, parity)
            return paths
        
        return traverse(root, 0)
