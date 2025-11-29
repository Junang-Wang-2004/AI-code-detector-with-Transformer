# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstToGst(self, root):
        stack = []
        curr = root
        accum = 0
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.right
            curr = stack.pop()
            curr.val += accum
            accum = curr.val
            curr = curr.left
        return root
