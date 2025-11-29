# Time:  O(n)
# Space: O(h)
class Solution2(object):
    def isUnivalTree(self, root):
        """
        """
        return (not root.left or (root.left.val == root.val and self.isUnivalTree(root.left))) and \
               (not root.right or (root.right.val == root.val and self.isUnivalTree(root.right)))
