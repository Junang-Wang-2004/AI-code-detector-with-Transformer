class C1(object):

    def lengthAfterTransformations(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [0] * 26
        for v3 in a1:
            v2[ord(v3) - ord('a')] += 1
        for v4 in range(a2):
            v5 = [0] * 26
            for v6 in range(26):
                v5[(v6 + 1) % 26] = (v5[(v6 + 1) % 26] + v2[v6]) % v1
                if v6 == 25:
                    v5[(v6 + 2) % 26] = (v5[(v6 + 2) % 26] + v2[v6]) % v1
            v2 = v5
        return reduce(lambda accu, x: (accu + v3) % v1, v2, 0)
