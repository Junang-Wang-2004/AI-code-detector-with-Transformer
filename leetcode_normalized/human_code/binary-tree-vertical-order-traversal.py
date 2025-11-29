import collections

class C1(object):

    def verticalOrder(self, a1):
        """
        """
        v1 = collections.defaultdict(list)
        v2 = [(a1, 0)]
        for v3, v4 in v2:
            if v3:
                v1[v4].append(v3.val)
                v2 += ((v3.left, v4 - 1), (v3.right, v4 + 1))
        return [v1[v4] for v4 in range(min(v1.keys()), max(v1.keys()) + 1)] if v1 else []
