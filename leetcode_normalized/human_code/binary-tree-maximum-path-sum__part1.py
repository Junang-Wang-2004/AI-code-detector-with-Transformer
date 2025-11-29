class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def maxPathSum(self, a1):

        def iter_dfs(a1):
            v1 = float('-inf')
            v2 = [0]
            v3 = [(1, [a1, v2])]
            while v3:
                v4, v5 = v3.pop()
                if v4 == 1:
                    a1, v7 = v5
                    if not a1:
                        continue
                    v8, v9 = ([0], [0])
                    v3.append((2, [a1, v8, v9, v7]))
                    v3.append((1, [a1.right, v9]))
                    v3.append((1, [a1.left, v8]))
                elif v4 == 2:
                    a1, v8, v9, v7 = v5
                    v1 = max(v1, a1.val + max(v8[0], 0) + max(v9[0], 0))
                    v7[0] = a1.val + max(v8[0], v9[0], 0)
            return v1
        return iter_dfs(a1)
