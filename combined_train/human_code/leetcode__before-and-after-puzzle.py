import collections

class C1(object):

    def beforeAndAfterPuzzles(self, a1):
        """
        """
        v1 = collections.defaultdict(list)
        for v2, v3 in enumerate(a1):
            v4 = v3.rfind(' ')
            v5 = v3 if v4 == -1 else v3[v4 + 1:]
            v1[v5].append(v2)
        v6 = set()
        for v2, v3 in enumerate(a1):
            v7 = v3.find(' ')
            v5 = v3 if v7 == -1 else v3[:v7]
            if v5 not in v1:
                continue
            for v8 in v1[v5]:
                if v8 == v2:
                    continue
                v6.add(a1[v8] + v3[len(v5):])
        return sorted(v6)
