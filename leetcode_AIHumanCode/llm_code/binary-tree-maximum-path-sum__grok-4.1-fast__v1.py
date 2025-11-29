class Solution:
    def maxPathSum(self, root):
        best = float('-inf')
        
        def path(node):
            nonlocal best
            if not node:
                return 0
            l = max(path(node.left), 0)
            r = max(path(node.right), 0)
            best = max(best, node.val + l + r)
            return node.val + max(l, r)
        
        path(root)
        return best
