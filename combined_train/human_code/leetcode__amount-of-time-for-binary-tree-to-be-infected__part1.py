class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        pass

class C2(object):

    def amountOfTime(self, a1, a2):
        """
        """

        def iter_dfs(a1, a2):
            v1 = -1
            v2 = [(1, (a1, [-1] * 2))]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    v5, v6 = v4
                    if v5 is None:
                        continue
                    v7, v8 = ([-1] * 2, [-1] * 2)
                    v2.append((2, (v5, v7, v8, v6)))
                    v2.append((1, (v5.right, v8)))
                    v2.append((1, (v5.left, v7)))
                elif v3 == 2:
                    v5, v7, v8, v6 = v4
                    v9 = -1
                    if v5.val == a2:
                        v9 = 0
                        v1 = max(v7[0], v8[0]) + 1
                    elif v7[1] >= 0:
                        v9 = v7[1] + 1
                        v1 = max(v1, v8[0] + 1 + v9)
                    elif v8[1] >= 0:
                        v9 = v8[1] + 1
                        v1 = max(v1, v7[0] + 1 + v9)
                    v6[:] = [max(v7[0], v8[0]) + 1, v9]
            return v1
        return iter_dfs(a1, a2)
