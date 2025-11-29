import itertools

class C1(object):

    def flipgame(self, a1, a2):
        """
        """
        v1 = {n for v2, v3 in enumerate(a1) if v3 == a2[v2]}
        v4 = float('inf')
        for v3 in itertools.chain(a1, a2):
            if v3 not in v1:
                v4 = min(v4, v3)
        return v4 if v4 < float('inf') else 0
