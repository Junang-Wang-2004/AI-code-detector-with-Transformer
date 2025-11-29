import bisect

class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        pass

class C2(object):

    def closestNodes(self, a1, a2):
        """
        """

        def iter_dfs():
            v1 = []
            v2 = [(1, a1)]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    if not v4:
                        continue
                    v2.append((1, v4.right))
                    v2.append((2, v4))
                    v2.append((1, v4.left))
                elif v3 == 2:
                    v1.append(v4.val)
            return v1
        v1 = iter_dfs()
        v2 = []
        for v3 in a2:
            v4 = bisect.bisect_left(v1, v3)
            if v4 == len(v1):
                v2.append([v1[v4 - 1], -1])
            elif v1[v4] == v3:
                v2.append([v1[v4], v1[v4]])
            elif v4 - 1 >= 0:
                v2.append([v1[v4 - 1], v1[v4]])
            else:
                v2.append([-1, v1[v4]])
        return v2
