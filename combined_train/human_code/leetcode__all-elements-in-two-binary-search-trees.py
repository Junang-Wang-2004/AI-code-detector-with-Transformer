class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def getAllElements(self, a1, a2):
        """
        """

        def inorder_gen(a1):
            v1, v2 = ([], [(a1, False)])
            while v2:
                a1, v4 = v2.pop()
                if a1 is None:
                    continue
                if v4:
                    yield a1.val
                else:
                    v2.append((a1.right, False))
                    v2.append((a1, True))
                    v2.append((a1.left, False))
            yield None
        v1 = []
        v2, v3 = (inorder_gen(a1), inorder_gen(a2))
        v4, v5 = (next(v2), next(v3))
        while v4 is not None or v5 is not None:
            if v5 is None or (v4 is not None and v4 < v5):
                v1.append(v4)
                v4 = next(v2)
            else:
                v1.append(v5)
                v5 = next(v3)
        return v1
