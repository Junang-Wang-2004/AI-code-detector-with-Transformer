class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2(object):

    def getDirections(self, a1, a2, a3):
        """
        """

        def iter_dfs(a1, a2):
            v1 = []
            v2 = [(1, (a1,))]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    v5 = v4[0]
                    if v5.val == a2:
                        v1.reverse()
                        return v1
                    for v6, v7 in enumerate((v5.left, v5.right)):
                        if not v7:
                            continue
                        v2.append((3, None))
                        v2.append((1, (v7,)))
                        v2.append((2, ('LR'[v6],)))
                elif v3 == 2:
                    v1.append(v4[0])
                elif v3 == 3:
                    v1.pop()
            return []
        v1 = iter_dfs(a1, a2)
        v2 = iter_dfs(a1, a3)
        while len(v1) and len(v2) and (v1[-1] == v2[-1]):
            v1.pop()
            v2.pop()
        v2.reverse()
        return ''.join(['U'] * len(v1) + v2)
