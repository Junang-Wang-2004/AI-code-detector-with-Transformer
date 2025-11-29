class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def isCousins(self, a1, a2, a3):
        v1 = [-1]
        v2 = [None]
        v3 = [-1]
        v4 = [None]

        def traverse(a1, a2, a3):
            if not a1:
                return
            if a1.val == a2:
                v1[0] = a3
                v2[0] = a2
            if a1.val == a3:
                v3[0] = a3
                v4[0] = a2
            traverse(a1.left, a1, a3 + 1)
            traverse(a1.right, a1, a3 + 1)
        traverse(a1, None, 0)
        return v1[0] == v3[0] and v2[0] != v4[0]
