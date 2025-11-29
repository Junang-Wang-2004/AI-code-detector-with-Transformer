v1 = [0, 1]

class C1(object):

    def makeStringSorted(self, a1):
        """
        """

        def inverse(a1, a2):
            v1 = len(v1)
            while len(v1) <= a1:
                v1.append(v1[a2 % v1] * (a2 - a2 // v1) % a2)
                v1 += 1
            return v1[a1]
        v1 = 10 ** 9 + 7
        v2, v3, v4 = ([0] * 26, 0, 1)
        for v5 in reversed(range(len(a1))):
            v6 = ord(a1[v5]) - ord('a')
            v2[v6] += 1
            v4 = v4 * (len(a1) - v5) * inverse(v2[v6], v1)
            v3 = (v3 + v4 * sum(v2[:v6]) * inverse(len(a1) - v5, v1)) % v1
        return v3
