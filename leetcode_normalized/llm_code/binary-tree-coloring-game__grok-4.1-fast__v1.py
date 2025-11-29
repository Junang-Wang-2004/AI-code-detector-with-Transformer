class C1:

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2:

    def btreeGameWinningMove(self, a1, a2, a3):

        def subtree_size(a1):
            if not a1:
                return 0
            return subtree_size(a1.left) + subtree_size(a1.right) + 1

        def search(a1):
            if not a1:
                return (None, 0, 0)
            if a1.val == a3:
                v1 = subtree_size(a1.left)
                v2 = subtree_size(a1.right)
                return (a1, v1, v2)
            v3 = search(a1.left)
            if v3[0]:
                return v3
            v3 = search(a1.right)
            if v3[0]:
                return v3
            return (None, 0, 0)
        v1, v2, v3 = search(a1)
        v4 = a2 - v2 - v3 - 1
        v5 = max(v2, v3, v4)
        return v5 > a2 - v5
