import collections

class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        pass

class C2(object):

    def treeQueries(self, a1, a2):
        """
        """

        def iter_dfs(a1):
            v1 = collections.defaultdict(lambda: [0] * 2)
            v2, v3 = ({}, {})
            v4 = [(1, (a1, 0))]
            while v4:
                v5, (v6, v7) = v4.pop()
                if v5 == 1:
                    if not v6:
                        continue
                    v4.append((2, (v6, v7)))
                    v4.append((1, (v6.right, v7 + 1)))
                    v4.append((1, (v6.left, v7 + 1)))
                elif v5 == 2:
                    v8 = 1 + max(v3[v6.left.val] if v6.left else 0, v3[v6.right.val] if v6.right else 0)
                    if v8 > v1[v7][0]:
                        v1[v7][0], v1[v7][1] = (v8, v1[v7][0])
                    elif v8 > v1[v7][1]:
                        v1[v7][1] = v8
                    v2[v6.val], v3[v6.val] = (v7, v8)
            return (v1, v2, v3)
        v1, v2, v3 = iter_dfs(a1)
        return [v2[q] - 1 + (v1[v2[q]][0] if v3[q] != v1[v2[q]][0] else v1[v2[q]][1]) for v4 in a2]
