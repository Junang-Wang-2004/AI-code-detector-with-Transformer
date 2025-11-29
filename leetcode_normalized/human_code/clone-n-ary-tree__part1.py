class C1(object):

    def __init__(self, a1=None, a2=None):
        self.val = a1
        self.children = a2 if a2 is not None else []

class C2(object):

    def cloneTree(self, a1):
        """
        """
        v1 = [None]
        v2 = [(1, (a1, v1))]
        while v2:
            v3, v4 = v2.pop()
            if v3 == 1:
                v5, v6 = v4
                if not v5:
                    continue
                v6[0] = C1(v5.val)
                for v7 in reversed(v5.children):
                    v8 = [None]
                    v2.append((2, (v8, v6)))
                    v2.append((1, (v7, v8)))
            else:
                v8, v6 = v4
                v6[0].children.append(v8[0])
        return v1[0]
