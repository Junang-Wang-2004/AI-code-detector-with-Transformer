class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def balanceBST(self, root):
        vals = []
        curr = root
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            vals.append(curr.val)
            curr = curr.right
        
        def build_tree(left, right):
            if left >= right:
                return None
            m = (left + right) // 2
            t = TreeNode(vals[m])
            t.left = build_tree(left, m)
            t.right = build_tree(m + 1, right)
            return t
        
        return build_tree(0, len(vals))
