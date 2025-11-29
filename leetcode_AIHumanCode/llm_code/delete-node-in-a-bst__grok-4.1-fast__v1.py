class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            pred = root.left
            while pred.right:
                pred = pred.right
            root.val = pred.val
            root.left = self.deleteNode(root.left, pred.val)

        return root
