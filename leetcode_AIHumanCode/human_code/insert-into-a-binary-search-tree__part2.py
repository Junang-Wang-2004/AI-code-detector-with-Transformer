# Time:  O(h)
# Space: O(h)
class Solution2(object):
    def insertIntoBST(self, root, val):
        """
        """
        if not root:
            root = TreeNode(val)
        else:
            if val <= root.val:
                root.left = self.insertIntoBST(root.left, val)
            else:
                root.right = self.insertIntoBST(root.right, val)
        return root

