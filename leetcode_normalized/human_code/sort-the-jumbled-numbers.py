class C1(object):

    def sortJumbled(self, a1, a2):
        """
        """

        def transform(a1, a2):
            if not a2:
                return a1[a2]
            v1, v2 = (0, 1)
            while a2:
                v1 += a1[a2 % 10] * v2
                a2 //= 10
                v2 *= 10
            return v1
        return [a2[i] for v1, v2 in sorted(((transform(a1, a2[v2]), v2) for v2 in range(len(a2))))]
