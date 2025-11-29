class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def rightSideView(self, a1):
        v1 = []
        self.rightSideViewDFS(a1, 1, v1)
        return v1

    def rightSideViewDFS(self, a1, a2, a3):
        if not a1:
            return
        if a2 > len(a3):
            a3.append(a1.val)
        self.rightSideViewDFS(a1.right, a2 + 1, a3)
        self.rightSideViewDFS(a1.left, a2 + 1, a3)
