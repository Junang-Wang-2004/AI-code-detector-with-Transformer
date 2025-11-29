class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        prev = None
        pright = None
        cur = root
        while cur:
            nxt = cur.left
            tmp_r = cur.right
            cur.left = pright
            cur.right = prev
            pright = tmp_r
            prev = cur
            cur = nxt
        return prev
