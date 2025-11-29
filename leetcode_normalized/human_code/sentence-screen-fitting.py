class C1(object):

    def wordsTyping(self, a1, a2, a3):
        """
        """

        def words_fit(a1, a2, a3):
            if len(a1[a2]) > a3:
                return 0
            v1, v2 = (len(a1[a2]), 1)
            v3 = (a2 + 1) % len(a1)
            while v1 + 1 + len(a1[v3]) <= a3:
                v1 += 1 + len(a1[v3])
                v2 += 1
                v3 = (v3 + 1) % len(a1)
            return v2
        v1 = [0] * len(a1)
        for v2 in range(len(a1)):
            v1[v2] = words_fit(a1, v2, a3)
        v3, v4 = (0, 0)
        for v2 in range(a2):
            v3 += v1[v4]
            v4 = (v4 + v1[v4]) % len(a1)
        return v3 / len(a1)
