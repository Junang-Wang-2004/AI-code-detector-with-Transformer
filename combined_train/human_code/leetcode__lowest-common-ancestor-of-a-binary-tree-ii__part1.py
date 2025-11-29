class C1(object):

    def __init__(self, a1):
        pass

class C2(object):

    def lowestCommonAncestor(self, a1, a2, a3):
        """
        """

        def iter_dfs(a1, a2, a3):
            v1 = None
            v2 = [(1, (a1, [0]))]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    a1, v6 = v4
                    if not a1:
                        continue
                    v7, v8 = ([0], [0])
                    v2.append((2, (a1, v7, v8, v6)))
                    v2.append((1, (a1.right, v8)))
                    v2.append((1, (a1.left, v7)))
                elif v3 == 2:
                    a1, v7, v8, v6 = v4
                    v9 = int(a1 == a2 or a1 == a3)
                    if v9 + v7[0] + v8[0] == 2 and (not v1):
                        v1 = a1
                    v6[0] = v9 + v7[0] + v8[0]
            return v1
        return iter_dfs(a1, a2, a3)
