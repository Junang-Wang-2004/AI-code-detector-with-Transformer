class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def levelOrder(self, a1):
        if a1 is None:
            return []
        v1, v2 = ([], [a1])
        while v2:
            v3, v4 = ([], [])
            for v5 in v2:
                v4.append(v5.val)
                if v5.left:
                    v3.append(v5.left)
                if v5.right:
                    v3.append(v5.right)
            v2 = v3
            v1.append(v4)
        return v1
