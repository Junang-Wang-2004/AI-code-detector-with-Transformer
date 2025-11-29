class C1(object):

    def arrayRankTransform(self, a1):
        """
        """
        return list(map({x: i + 1 for v1, v2 in enumerate(sorted(set(a1)))}.get, a1))
