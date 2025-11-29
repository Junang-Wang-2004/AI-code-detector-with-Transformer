class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        pass

class C2(object):

    def averageOfSubtree(self, a1):
        """
        """

        def iter_dfs(a1):
            v1 = 0
            v2 = [(1, (a1, [0] * 2))]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    v5, v6 = v4
                    if not v5:
                        continue
                    v7, v8 = ([0] * 2, [0] * 2)
                    v2.append((2, (v5, v7, v8, v6)))
                    v2.append((1, (v5.right, v8)))
                    v2.append((1, (v5.left, v7)))
                elif v3 == 2:
                    v5, v7, v8, v6 = v4
                    v6[0] = v7[0] + v8[0] + v5.val
                    v6[1] = v7[1] + v8[1] + 1
                    v1 += int(v6[0] // v6[1] == v5.val)
            return v1
        return iter_dfs(a1)
