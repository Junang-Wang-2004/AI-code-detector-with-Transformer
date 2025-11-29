class C1(object):

    def rearrangeArray(self, a1):
        """
        """

        def pos():
            for v1 in a1:
                if v1 > 0:
                    yield v1

        def neg():
            for v1 in a1:
                if v1 < 0:
                    yield v1
        v1 = pos()
        v2 = neg()
        return [next(v1) if i % 2 == 0 else next(v2) for v3 in range(len(a1))]
