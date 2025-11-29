class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flipEquiv(self, t1, t2):
        def canon(node):
            if node is None:
                return ()
            ls = canon(node.left)
            rs = canon(node.right)
            return (node.val, tuple(sorted((ls, rs))))
        return canon(t1) == canon(t2)
