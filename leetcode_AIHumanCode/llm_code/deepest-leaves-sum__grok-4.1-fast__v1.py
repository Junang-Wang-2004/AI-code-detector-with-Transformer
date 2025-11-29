# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deepestLeavesSum(self, root):
        if not root:
            return 0
        layer = [root]
        while layer:
            nxt_layer = []
            for nd in layer:
                if nd.left:
                    nxt_layer.append(nd.left)
                if nd.right:
                    nxt_layer.append(nd.right)
            if not nxt_layer:
                return sum(nd.val for nd in layer)
            layer = nxt_layer
