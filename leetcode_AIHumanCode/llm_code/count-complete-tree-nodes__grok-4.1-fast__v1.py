class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass

class Solution(object):
    def countNodes(self, root):
        def left_depth(curr):
            dep = -1
            while curr:
                dep += 1
                curr = curr.left
            return dep

        def total_nodes(curr):
            if not curr:
                return 0
            ldep = left_depth(curr.left)
            rdep = left_depth(curr.right)
            if ldep == rdep:
                return (1 << (ldep + 2)) - 1
            return 1 + total_nodes(curr.left) + total_nodes(curr.right)

        return total_nodes(root)
