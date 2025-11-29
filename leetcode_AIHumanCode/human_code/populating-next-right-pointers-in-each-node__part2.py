# Time:  O(n)
# Space: O(logn)
# recusion
class Solution2(object):
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        if root.left:
            root.left.next = root.right
        if root.right and root.__next__:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

