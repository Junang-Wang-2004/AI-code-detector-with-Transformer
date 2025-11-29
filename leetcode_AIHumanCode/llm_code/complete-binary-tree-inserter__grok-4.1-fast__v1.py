from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CBTInserter:
    def __init__(self, root):
        self.root = root
        self.ready = deque()
        q = deque([root])
        while q:
            curr = q.popleft()
            if curr.left is None or curr.right is None:
                self.ready.append(curr)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

    def insert(self, v):
        par = self.ready[0]
        child = TreeNode(v)
        if par.left is None:
            par.left = child
        else:
            par.right = child
            self.ready.popleft()
        self.ready.append(child)
        return par.val

    def get_root(self):
        return self.root
