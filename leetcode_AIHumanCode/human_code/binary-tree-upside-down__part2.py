# Time:  O(n)
# Space: O(n)
class Solution2(object):
    # @param root, a tree node
    # @return root of the upside down tree
    def upsideDownBinaryTree(self, root):
        return self.upsideDownBinaryTreeRecu(root, None)

    def upsideDownBinaryTreeRecu(self, p, parent):
        if p is None:
            return parent

        root = self.upsideDownBinaryTreeRecu(p.left, p)
        if parent:
            p.left = parent.right
        else:
            p.left = None
        p.right = parent

        return root

