class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root):
        count = 0
        def postorder(node):
            nonlocal count
            if node is None:
                return 1
            lstate = postorder(node.left)
            rstate = postorder(node.right)
            if lstate == 0 or rstate == 0:
                count += 1
                return 2
            elif lstate == 2 or rstate == 2:
                return 1
            return 0
        gre = postorder(root)
        if gre == 0:
            count += 1
        return count
