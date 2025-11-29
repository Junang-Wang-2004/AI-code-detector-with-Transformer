class C1(object):

    def placeWordInCrossword(self, a1, a2):
        """
        """

        def get_val(a1, a2, a3, a4):
            return a1[a2][a3] if not a4 else a1[a3][a2]

        def get_vecs(a1, a2):
            for v1 in range(len(a1) if not a2 else len(a1[0])):
                yield (get_val(a1, v1, j, a2) for v2 in range(len(a1[0]) if not a2 else len(a1)))
        for v1 in (lambda x: iter(x), reversed):
            for v2 in range(2):
                for v3 in get_vecs(a1, v2):
                    v4, v5 = (v1(a2), True)
                    for v6 in v3:
                        if v6 == '#':
                            if next(v4, None) is None and v5:
                                return True
                            v4, v5 = (v1(a2), True)
                            continue
                        if not v5:
                            continue
                        v7 = next(v4, None)
                        v5 = v7 is not None and v6 in (v7, ' ')
                    if next(v4, None) is None and v5:
                        return True
        return False
