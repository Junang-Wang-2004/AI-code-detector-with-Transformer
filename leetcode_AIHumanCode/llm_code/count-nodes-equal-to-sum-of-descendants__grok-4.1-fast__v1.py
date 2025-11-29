# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def equalToDescendants(self, root):
        def traverse(curr):
            if not curr:
                return 0, 0
            lcount, lsum = traverse(curr.left)
            rcount, rsum = traverse(curr.right)
            desum = lsum + rsum
            count = lcount + rcount + (1 if curr.val == desum else 0)
            return count, desum + curr.val
        
        if not root:
            return 0
        return traverse(root)[0]
