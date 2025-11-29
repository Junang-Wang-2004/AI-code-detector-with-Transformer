class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        pass

class C2(object):

    def equalToDescendants(self, a1):
        """
        """

        def iter_dfs(a1):
            v1 = 0
            v2 = [(1, [a1, [0]])]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    a1, v6 = v4
                    if not a1:
                        continue
                    v7, v8 = ([0], [0])
                    v2.append((2, [a1, v7, v8, v6]))
                    v2.append((1, [a1.right, v8]))
                    v2.append((1, [a1.left, v7]))
                elif v3 == 2:
                    a1, v7, v8, v6 = v4
                    if a1.val == v7[0] + v8[0]:
                        v1 += 1
                    v6[0] = v7[0] + v8[0] + a1.val
            return v1
        return iter_dfs(a1)
