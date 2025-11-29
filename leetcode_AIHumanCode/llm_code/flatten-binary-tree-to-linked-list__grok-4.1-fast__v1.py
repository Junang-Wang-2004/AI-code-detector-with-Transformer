class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        curr = root
        while curr:
            if curr.left:
                pred = curr.left
                while pred.right:
                    pred = pred.right
                pred.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right
