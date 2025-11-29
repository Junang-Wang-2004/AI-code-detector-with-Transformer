class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def balanceBST(self, a1):
        """
        """

        def inorderTraversal(a1):
            v1, v2 = ([], [(a1, False)])
            while v2:
                v3, v4 = v2.pop()
                if v3 is None:
                    continue
                if v4:
                    v1.append(v3.val)
                else:
                    v2.append((v3.right, False))
                    v2.append((v3, True))
                    v2.append((v3.left, False))
            return v1

        def sortedArrayToBst(a1):
            v1, v2, v3 = list(range(3))
            v4 = [None]
            v5 = [(0, len(a1), v1, v4)]
            while v5:
                v6, v7, v8, v9 = v5.pop()
                if v6 >= v7:
                    continue
                v10 = v6 + (v7 - v6) // 2
                v11 = C1(a1[v10])
                if v8 == v1:
                    v9[0] = v11
                elif v8 == v2:
                    v9[0].left = v11
                else:
                    v9[0].right = v11
                v5.append((v10 + 1, v7, v3, [v11]))
                v5.append((v6, v10, v2, [v11]))
            return v4[0]
        return sortedArrayToBst(inorderTraversal(a1))
