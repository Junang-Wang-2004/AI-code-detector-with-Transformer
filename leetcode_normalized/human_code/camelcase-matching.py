class C1(object):

    def camelMatch(self, a1, a2):
        """
        """

        def is_matched(a1, a2):
            v1 = 0
            for v2 in a1:
                if v1 < len(a2) and a2[v1] == v2:
                    v1 += 1
                elif v2.isupper():
                    return False
            return v1 == len(a2)
        v1 = []
        for v2 in a1:
            v1.append(is_matched(v2, a2))
        return v1
