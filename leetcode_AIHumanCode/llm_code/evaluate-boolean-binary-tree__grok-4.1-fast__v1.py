class Solution:
    def evaluateTree(self, root):
        def process(n):
            if n.val <= 1:
                return n.val
            lval = process(n.left)
            rval = process(n.right)
            if n.val == 2:
                return lval or rval
            return lval and rval

        return process(root)
