class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isEvenOddTree(self, root):
        q = [root] if root else []
        lv = 0
        while q:
            nxt = []
            vals = []
            for nd in q:
                vals.append(nd.val)
                if nd.left:
                    nxt.append(nd.left)
                if nd.right:
                    nxt.append(nd.right)
            for j in range(len(vals)):
                v = vals[j]
                if lv % 2 == 0:
                    if v % 2 == 0 or (j > 0 and vals[j - 1] >= v):
                        return False
                else:
                    if v % 2 != 0 or (j > 0 and vals[j - 1] <= v):
                        return False
            q = nxt
            lv += 1
        return True
