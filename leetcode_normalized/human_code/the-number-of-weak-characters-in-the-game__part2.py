import collections

class C1(object):

    def numberOfWeakCharacters(self, a1):
        """
        """
        v1 = collections.defaultdict(list)
        for v2, v3 in a1:
            v1[v2].append(v3)
        v4 = v5 = 0
        for v2 in sorted(iter(v1.keys()), reverse=True):
            v4 += sum((v3 < v5 for v3 in v1[v2]))
            v5 = max(v5, max(v1[v2]))
        return v4
