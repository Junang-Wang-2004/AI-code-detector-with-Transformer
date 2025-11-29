class C1(object):

    def numberOfSubstrings(self, a1, a2):
        """
        """

        def count():
            v1 = [0] * 26
            v2 = v3 = 0
            for v4 in range(len(a1)):
                v1[ord(a1[v4]) - ord('a')] += 1
                while v1[ord(a1[v4]) - ord('a')] == a2:
                    v1[ord(a1[v3]) - ord('a')] -= 1
                    v3 += 1
                v2 += v4 - v3 + 1
            return v2
        return (len(a1) + 1) * len(a1) // 2 - count()
