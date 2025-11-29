class C1:

    def __next__(self):
        pass

class C2(object):

    def findPattern(self, a1, a2):
        """
        """

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
        v1 = getPrefix(a2)
        v2 = v3 = -1
        while True:
            v4 = next(a1)
            v2 += 1
            while v3 + 1 > 0 and a2[v3 + 1] != v4:
                v3 = v1[v3]
            if a2[v3 + 1] == v4:
                v3 += 1
            if v3 + 1 == len(a2):
                return v2 - v3
        return -1
