import collections

class C1(object):

    def maxArea(self, a1):
        """
        """
        v1 = max((x for v2, v3 in a1))
        v4 = min((v2 for v2, v3 in a1))
        v5 = max((y for v3, v6 in a1))
        v7 = min((v6 for v3, v6 in a1))
        v8 = collections.defaultdict(lambda: float('-inf'))
        v9 = collections.defaultdict(lambda: float('inf'))
        v10 = collections.defaultdict(lambda: float('-inf'))
        v11 = collections.defaultdict(lambda: float('inf'))
        for v2, v6 in a1:
            v8[v2] = max(v8[v2], v6)
            v9[v2] = min(v9[v2], v6)
            v10[v6] = max(v10[v6], v2)
            v11[v6] = min(v11[v6], v2)
        v12 = max(max(((v8[v2] - v9[v2]) * max(v2 - v4, v1 - v2) for v2 in v8.keys())), max(((v10[v6] - v11[v6]) * max(v6 - v7, v5 - v6) for v6 in v10.keys())))
        return v12 if v12 else -1
