class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def increasingBST(self, root):
        def traverse(curr):
            nonlocal start, prev_node
            if not curr:
                return
            traverse(curr.left)
            if prev_node:
                prev_node.right = curr
            else:
                start = curr
            curr.left = None
            prev_node = curr
            traverse(curr.right)

        start = prev_node = None
        traverse(root)
        return start
