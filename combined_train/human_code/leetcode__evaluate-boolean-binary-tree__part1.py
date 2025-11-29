class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        pass

class C2(object):

    def evaluateTree(self, a1):
        """
        """
        v1 = float('inf')
        v2 = {2: lambda x, y: x or y, 3: lambda x, y: x and y}

        def iter_dfs(a1):
            v1 = [0]
            v2 = [(1, (a1, v1))]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    v5, v1 = v4
                    if v5.left == v5.right:
                        v1[0] = v5.val
                        continue
                    v6, v7 = ([0], [0])
                    v2.append((2, (v5, v6, v7, v1)))
                    v2.append((1, (v5.right, v7)))
                    v2.append((1, (v5.left, v6)))
                elif v3 == 2:
                    v5, v6, v7, v1 = v4
                    v1[0] = v2[v5.val](v6[0], v7[0])
            return v1[0]
        return iter_dfs(a1)
