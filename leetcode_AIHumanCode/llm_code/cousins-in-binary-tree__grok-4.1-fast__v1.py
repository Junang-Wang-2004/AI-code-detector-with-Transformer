class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        x_depth = [-1]
        x_parent = [None]
        y_depth = [-1]
        y_parent = [None]

        def traverse(curr, par, lev):
            if not curr:
                return
            if curr.val == x:
                x_depth[0] = lev
                x_parent[0] = par
            if curr.val == y:
                y_depth[0] = lev
                y_parent[0] = par
            traverse(curr.left, curr, lev + 1)
            traverse(curr.right, curr, lev + 1)

        traverse(root, None, 0)
        return x_depth[0] == y_depth[0] and x_parent[0] != y_parent[0]
