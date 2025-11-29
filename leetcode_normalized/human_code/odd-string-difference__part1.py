import collections

class C1(object):

    def oddString(self, a1):
        """
        """
        for v1 in range(len(a1[0]) - 1):
            v2 = collections.defaultdict(list)
            for v3, v4 in enumerate(a1):
                if len(v2[ord(v4[v1 + 1]) - ord(v4[v1])]) < 2:
                    v2[ord(v4[v1 + 1]) - ord(v4[v1])].append(v3)
            if len(v2) == 2:
                return next((a1[l[0]] for v5 in v2.values() if len(v5) == 1))
