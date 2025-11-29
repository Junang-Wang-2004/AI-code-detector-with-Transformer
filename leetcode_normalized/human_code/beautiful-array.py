class C1(object):

    def beautifulArray(self, a1):
        """
        """
        v1 = [1]
        while len(v1) < a1:
            v1 = [i * 2 - 1 for v2 in v1] + [v2 * 2 for v2 in v1]
        return [v2 for v2 in v1 if v2 <= a1]
