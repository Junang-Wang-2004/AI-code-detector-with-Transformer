class C1(object):

    def shuffle(self, a1, a2):
        """
        """

        def index(a1):
            return 2 * a1 if a1 < a2 else 2 * (a1 - a2) + 1
        for v1 in range(len(a1)):
            v2 = v1
            while a1[v1] >= 0:
                v2 = index(v2)
                a1[v1], a1[v2] = (a1[v2], ~a1[v1])
        for v1 in range(len(a1)):
            a1[v1] = ~a1[v1]
        return a1
