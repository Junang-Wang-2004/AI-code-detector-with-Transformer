class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def bstFromPreorder(self, a1):
        if not a1:
            return None
        v1 = C1(a1[0])
        v2 = [v1]
        for v3 in a1[1:]:
            v4 = C1(v3)
            if v3 < v2[-1].val:
                v2[-1].left = v4
            else:
                v5 = None
                while v2 and v2[-1].val < v3:
                    v5 = v2.pop()
                v5.right = v4
            v2.append(v4)
        return v1
