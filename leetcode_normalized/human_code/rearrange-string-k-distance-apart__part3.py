import collections
import itertools

class C1(object):

    def rearrangeString(self, a1, a2):
        """
        """
        v1 = collections.Counter(a1)
        v2 = max(v1.values())
        v3 = [[] for v4 in range(v2)]
        v5 = 0
        for v6 in itertools.chain((v6 for v6, v7 in v1.items() if v7 == v2), (v6 for v6, v7 in v1.items() if v7 == v2 - 1), (v6 for v6, v7 in v1.items() if v7 <= v2 - 2)):
            for v4 in range(v1[v6]):
                v3[v5].append(v6)
                v5 = (v5 + 1) % max(v1[v6], v2 - 1)
        if any((len(v3[v5]) < a2 for v5 in range(len(v3) - 1))):
            return ''
        return ''.join([''.join(x) for v8 in v3])
