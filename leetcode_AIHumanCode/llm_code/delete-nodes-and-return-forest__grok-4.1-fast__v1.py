class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def delNodes(self, root, to_delete):
        targets = set(to_delete)
        roots = []
        def process(curr):
            if curr is None:
                return None
            curr.left = process(curr.left)
            curr.right = process(curr.right)
            if curr.val in targets:
                if curr.left is not None:
                    roots.append(curr.left)
                if curr.right is not None:
                    roots.append(curr.right)
                return None
            return curr
        head = process(root)
        if head is not None:
            roots.append(head)
        return roots
