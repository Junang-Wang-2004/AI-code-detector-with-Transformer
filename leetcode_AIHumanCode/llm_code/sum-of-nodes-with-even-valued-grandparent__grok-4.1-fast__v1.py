class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root):
        res = 0
        stk = []
        if root:
            stk.append((root, None, None))
        while stk:
            curr, par_val, gpar_val = stk.pop()
            if gpar_val is not None and gpar_val % 2 == 0:
                res += curr.val
            if curr.right:
                stk.append((curr.right, curr.val, par_val))
            if curr.left:
                stk.append((curr.left, curr.val, par_val))
        return res
