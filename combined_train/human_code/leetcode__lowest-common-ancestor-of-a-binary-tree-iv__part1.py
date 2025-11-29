class C1(object):

    def __init__(self, a1):
        pass

class C2(object):

    def lowestCommonAncestor(self, a1, a2):
        """
        """

        def iter_dfs(a1, a2):
            v1 = [0]
            v2 = [(1, (a1, v1))]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    v5, v6 = v4
                    if not v5 or v5 in a2:
                        v6[0] = v5
                        continue
                    v7, v8 = ([None], [None])
                    v2.append((2, (v5, v7, v8, v6)))
                    v2.append((1, (v5.right, v8)))
                    v2.append((1, (v5.left, v7)))
                elif v3 == 2:
                    v5, v7, v8, v6 = v4
                    if v7[0] and v8[0]:
                        v6[0] = v5
                    else:
                        v6[0] = v7[0] or v8[0]
            return v1[0]
        return iter_dfs(a1, set(a2))
