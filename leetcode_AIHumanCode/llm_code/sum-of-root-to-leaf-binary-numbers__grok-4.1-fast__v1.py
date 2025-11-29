class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        MOD = 10**9 + 7
        if not root:
            return 0
        result = 0
        stk = [(root, 0)]
        while stk:
            node, accum = stk.pop()
            accum = ((accum << 1) + node.val) % MOD
            if not node.left and not node.right:
                result = (result + accum) % MOD
            else:
                if node.right:
                    stk.append((node.right, accum))
                if node.left:
                    stk.append((node.left, accum))
        return result
