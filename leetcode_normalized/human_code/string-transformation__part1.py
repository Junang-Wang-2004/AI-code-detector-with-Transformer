from functools import reduce

class C1(object):

    def numberOfWays(self, a1, a2, a3):
        """
        """
        v1 = 10 ** 9 + 7

        def getPrefix(a1):
            v1 = [-1] * len(a1)
            v2 = -1
            for v3 in range(1, len(a1)):
                while v2 + 1 > 0 and a1[v2 + 1] != a1[v3]:
                    v2 = v1[v2]
                if a1[v2 + 1] == a1[v3]:
                    v2 += 1
                v1[v3] = v2
            return v1

        def KMP(a1, a2):
            v1 = getPrefix(a2)
            v2 = -1
            for v3 in range(len(a1)):
                while v2 + 1 > 0 and a2[v2 + 1] != a1[v3]:
                    v2 = v1[v2]
                if a2[v2 + 1] == a1[v3]:
                    v2 += 1
                if v2 + 1 == len(a2):
                    yield (v3 - v2)
                    v2 = v1[v2]
        v2 = len(a1)
        v3 = [0] * 2
        v3[1] = (pow(v2 - 1, a3, v1) - (-1) ** a3) * pow(v2, v1 - 2, v1) % v1
        v3[0] = (v3[1] + (-1) ** a3) % v1
        return reduce(lambda a, b: (a + b) % v1, (v3[int(i != 0)] for v4 in KMP(a1 + a1[:-1], a2)), 0)
