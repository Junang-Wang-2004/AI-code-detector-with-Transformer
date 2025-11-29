class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def btreeGameWinningMove(self, root, n, x):
        def subtree_size(curr):
            if not curr:
                return 0
            return subtree_size(curr.left) + subtree_size(curr.right) + 1

        def search(curr):
            if not curr:
                return None, 0, 0
            if curr.val == x:
                lsz = subtree_size(curr.left)
                rsz = subtree_size(curr.right)
                return curr, lsz, rsz
            res = search(curr.left)
            if res[0]:
                return res
            res = search(curr.right)
            if res[0]:
                return res
            return None, 0, 0

        _, lsz, rsz = search(root)
        restsz = n - lsz - rsz - 1
        largest = max(lsz, rsz, restsz)
        return largest > n - largest
