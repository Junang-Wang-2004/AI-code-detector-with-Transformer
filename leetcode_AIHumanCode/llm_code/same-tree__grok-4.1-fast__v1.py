class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        stk = [(p, q)]
        while stk:
            node1, node2 = stk.pop()
            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None or node1.val != node2.val:
                return False
            stk.append((node1.right, node2.right))
            stk.append((node1.left, node2.left))
        return True
