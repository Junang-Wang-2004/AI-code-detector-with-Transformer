class C1(object):

    def shortestSequence(self, a1, a2):
        """
        """
        v1 = 0
        v2 = set()
        for v3 in a1:
            v2.add(v3)
            if len(v2) != a2:
                continue
            v2.clear()
            v1 += 1
        return v1 + 1
