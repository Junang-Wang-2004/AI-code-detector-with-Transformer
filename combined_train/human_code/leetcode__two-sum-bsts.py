class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def twoSumBSTs(self, a1, a2, a3):
        """
        """

        def inorder_gen(a1, a2=True):
            v1, v2 = ([], [(a1, False)])
            while v2:
                a1, v4 = v2.pop()
                if a1 is None:
                    continue
                if v4:
                    yield a1.val
                elif a2:
                    v2.append((a1.right, False))
                    v2.append((a1, True))
                    v2.append((a1.left, False))
                else:
                    v2.append((a1.left, False))
                    v2.append((a1, True))
                    v2.append((a1.right, False))
        v1, v2 = (inorder_gen(a1, True), inorder_gen(a2, False))
        v3, v4 = (next(v1), next(v2))
        while v3 is not None and v4 is not None:
            if v3 + v4 < a3:
                v3 = next(v1)
            elif v3 + v4 > a3:
                v4 = next(v2)
            else:
                return True
        return False
