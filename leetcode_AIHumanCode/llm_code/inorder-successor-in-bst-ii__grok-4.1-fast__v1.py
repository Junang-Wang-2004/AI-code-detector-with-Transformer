class Node:
    def __init__(self, val, left, right, parent):
        self.val, self.left, self.right, self.parent = val, left, right, parent

class Solution:
    def inorderSuccessor(self, n):
        if n is None:
            return None
        if n.right:
            succ = n.right
            while succ.left:
                succ = succ.left
            return succ
        p = n.parent
        while p and p.right == n:
            n = p
            p = p.parent
        return p
