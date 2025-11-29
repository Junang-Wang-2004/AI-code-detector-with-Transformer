class C1(object):

    def minimumString(self, a1, a2, a3):
        """
        """

        def merge(a1, a2):
            if a1 in a2:
                return a2
            v1 = next((v1 for v1 in reversed(range(1, min(len(a1), len(a2)))) if a1[-v1:] == a2[:v1]), 0)
            return a1 + a2[v1:]
        v1 = [merge(a1, merge(a2, a3)), merge(a1, merge(a3, a2)), merge(a2, merge(a1, a3)), merge(a2, merge(a3, a1)), merge(a3, merge(a1, a2)), merge(a3, merge(a2, a1))]
        return min(v1, key=lambda x: (len(x), x))
