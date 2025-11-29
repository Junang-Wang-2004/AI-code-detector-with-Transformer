import collections

class C1(object):

    def convertArray(self, a1):
        """
        """
        v1 = sorted(set(a1))

        def f(a1):
            v1 = collections.defaultdict(int)
            for v2 in a1:
                v3 = -1
                for v4 in v1:
                    v1[v4] = min(v1[v4] + abs(v4 - v2), v1[v3]) if v3 != -1 else v1[v4] + abs(v4 - v2)
                    v3 = v4
            return v1[v1[-1]]
        return min(f(a1), f((x for v2 in reversed(a1))))
