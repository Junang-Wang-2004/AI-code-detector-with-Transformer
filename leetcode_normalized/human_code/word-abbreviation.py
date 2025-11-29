import collections

class C1(object):

    def wordsAbbreviation(self, a1):
        """
        """

        def isUnique(a1, a2):
            return sum((word.startswith(a1) for v1 in a2)) == 1

        def toAbbr(a1, a2):
            v1 = a1 + str(len(a2) - 1 - len(a1)) + a2[-1]
            return v1 if len(v1) < len(a2) else a2
        v1 = collections.defaultdict(set)
        v2 = {}
        for v3 in a1:
            v4 = v3[:1]
            v1[toAbbr(v4, v3)].add(v3)
        for v5, v6 in v1.items():
            if len(v6) > 1:
                for v3 in v6:
                    for v7 in range(2, len(v3)):
                        v4 = v3[:v7]
                        if isUnique(v4, v6):
                            v2[v3] = toAbbr(v4, v3)
                            break
            else:
                v2[v6.pop()] = v5
        return [v2[v3] for v3 in a1]
