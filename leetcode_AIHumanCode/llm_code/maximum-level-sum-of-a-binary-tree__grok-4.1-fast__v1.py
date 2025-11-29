class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def maxLevelSum(self, root):
        totals = []
        pending = [root]
        while pending:
            nxt = []
            sm = 0
            for nd in pending:
                sm += nd.val
                if nd.left:
                    nxt.append(nd.left)
                if nd.right:
                    nxt.append(nd.right)
            totals.append(sm)
            pending = nxt
        peak = max(totals)
        return totals.index(peak) + 1
