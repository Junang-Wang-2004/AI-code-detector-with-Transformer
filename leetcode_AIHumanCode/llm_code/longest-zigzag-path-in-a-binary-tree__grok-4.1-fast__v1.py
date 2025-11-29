class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root):
        self.best = 0
        def explore(u):
            if u is None:
                return -1, -1
            cleft, cright = explore(u.left)
            dleft, dright = explore(u.right)
            straight_left = 1 + cright
            straight_right = 1 + dleft
            self.best = max(self.best, straight_left, straight_right)
            return straight_left, straight_right
        explore(root)
        return self.best
