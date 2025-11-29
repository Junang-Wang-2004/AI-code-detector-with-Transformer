class Solution(object):
    def lowestCommonAncestor(self, curr, x, y):
        if curr is None:
            return None
        if curr == x or curr == y:
            return curr
        lca_left = self.lowestCommonAncestor(curr.left, x, y)
        lca_right = self.lowestCommonAncestor(curr.right, x, y)
        if lca_left and lca_right:
            return curr
        return lca_left or lca_right
