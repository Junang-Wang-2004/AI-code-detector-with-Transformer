class C1(object):

    def findAllConcatenatedWordsInADict(self, a1):
        """
        """
        v1 = set(a1)
        v2 = []
        for v3 in a1:
            v4 = [False] * (len(v3) + 1)
            v4[0] = True
            for v5 in range(len(v3)):
                if not v4[v5]:
                    continue
                for v6 in range(v5 + 1, len(v3) + 1):
                    if v6 - v5 < len(v3) and v3[v5:v6] in v1:
                        v4[v6] = True
                if v4[len(v3)]:
                    v2.append(v3)
                    break
        return v2
