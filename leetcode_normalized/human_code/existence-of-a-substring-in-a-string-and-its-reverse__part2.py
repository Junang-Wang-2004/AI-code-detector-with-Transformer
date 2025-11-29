import collections

class C1(object):

    def isSubstringPresent(self, a1):
        """
        """
        v1 = collections.defaultdict(set)
        for v2 in range(len(a1) - 1):
            v1[a1[v2]].add(a1[v2 + 1])
        return any((a1[v2] in v1[a1[v2 + 1]] for v2 in range(len(a1) - 1)))
