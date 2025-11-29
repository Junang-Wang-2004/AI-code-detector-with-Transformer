import collections

class C1(object):

    def numMatchingSubseq(self, a1, a2):
        """
        """
        v1 = collections.defaultdict(list)
        for v2 in a2:
            v3 = iter(v2)
            v1[next(v3, None)].append(v3)
        for v4 in a1:
            for v3 in v1.pop(v4, ()):
                v1[next(v3, None)].append(v3)
        return len(v1[None])
