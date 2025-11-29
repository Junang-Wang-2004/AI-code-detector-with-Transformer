class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root is None or root == p or root == q:
            return root
        left_res = self.lowestCommonAncestor(root.left, p, q)
        right_res = self.lowestCommonAncestor(root.right, p, q)
        if left_res and right_res:
            return root
        return left_res if left_res else right_res
