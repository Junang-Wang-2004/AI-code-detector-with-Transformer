class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        pass

class C2(object):

    def findDistance(self, a1, a2, a3):
        """
        """

        def iter_dfs(a1, a2, a3):
            v1 = 0
            v2 = [-1]
            v3 = [(1, [a1, v2])]
            while v3:
                v4, v5 = v3.pop()
                if v4 == 1:
                    v6, v7 = v5
                    if not v6:
                        continue
                    v8, v9 = ([-1], [-1])
                    v3.append((2, [v6, v8, v9, v7]))
                    v3.append((1, [v6.right, v9]))
                    v3.append((1, [v6.left, v8]))
                elif v4 == 2:
                    v6, v8, v9, v7 = v5
                    if v6.val in (a2, a3):
                        if v8[0] == v9[0] == -1:
                            v7[0] = 0
                        else:
                            v1 = v8[0] + 1 if v8[0] != -1 else v9[0] + 1
                    elif v8[0] != -1 and v9[0] != -1:
                        v1 = v8[0] + v9[0] + 2
                    elif v8[0] != -1:
                        v7[0] = v8[0] + 1
                    elif v9[0] != -1:
                        v7[0] = v9[0] + 1
            return v1
        return iter_dfs(a1, a2, a3)
