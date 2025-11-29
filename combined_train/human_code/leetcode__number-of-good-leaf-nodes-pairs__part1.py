import collections

class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2(object):

    def countPairs(self, a1, a2):
        """
        """

        def iter_dfs(a1, a2):
            v1 = 0
            v2 = [(1, (a2, [collections.Counter()]))]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    v5, v6 = v4
                    if not v5:
                        continue
                    if not v5.left and (not v5.right):
                        v6[0][0] = 1
                        continue
                    v7, v8 = ([collections.Counter()], [collections.Counter()])
                    v2.append((2, (v7, v8, v6)))
                    v2.append((1, (v5.right, v8)))
                    v2.append((1, (v5.left, v7)))
                else:
                    v7, v8, v6 = v4
                    for v9, v10 in v7[0].items():
                        for v11, v12 in v8[0].items():
                            if v9 + v11 + 2 <= a1:
                                v1 += v10 * v12
                    v6[0] = collections.Counter({k + 1: v for v13, v14 in (v7[0] + v8[0]).items()})
            return v1
        return iter_dfs(a2, a1)
