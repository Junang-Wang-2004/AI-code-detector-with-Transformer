import itertools

class C1(object):

    def shortestToChar(self, a1, a2):
        """
        """
        v1 = [len(a1)] * len(a1)
        v2 = -len(a1)
        for v3 in itertools.chain(range(len(a1)), reversed(range(len(a1)))):
            if a1[v3] == a2:
                v2 = v3
            v1[v3] = min(v1[v3], abs(v3 - v2))
        return v1
