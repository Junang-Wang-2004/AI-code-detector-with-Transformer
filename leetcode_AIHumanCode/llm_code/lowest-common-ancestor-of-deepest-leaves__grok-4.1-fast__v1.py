class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lcaDeepestLeaves(self, root):
        def dfs(curr):
            if not curr:
                return 0, None
            l_depth, l_node = dfs(curr.left)
            r_depth, r_node = dfs(curr.right)
            max_sub = max(l_depth, r_depth)
            if l_depth == max_sub and r_depth == max_sub:
                return max_sub + 1, curr
            if l_depth == max_sub:
                return max_sub + 1, l_node
            return max_sub + 1, r_node

        return dfs(root)[1]
