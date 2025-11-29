class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distributeCoins(self, root):
        def traverse(node):
            if not node:
                return 0, 0
            l_excess, l_cost = traverse(node.left)
            r_excess, r_cost = traverse(node.right)
            extra_cost = abs(l_excess) + abs(r_excess)
            total_cost = l_cost + r_cost + extra_cost
            excess = node.val + l_excess + r_excess - 1
            return excess, total_cost
        _, moves = traverse(root)
        return moves
