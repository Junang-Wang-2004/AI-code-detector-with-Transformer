import collections
import itertools

class C1(object):

    def rearrangeString(self, a1, a2):
        """
        """
        if not a2:
            return a1
        v1 = collections.Counter(a1)
        v2 = max(v1.values())
        if not (v2 - 1) * a2 + sum((x == v2 for v3 in v1.values())) <= len(a1):
            return ''
        v4 = [0] * len(a1)
        v5 = (len(a1) - 1) % a2
        for v6 in itertools.chain((v6 for v6, v7 in v1.items() if v7 == v2), (v6 for v6, v7 in v1.items() if v7 != v2)):
            for v8 in range(v1[v6]):
                v4[v5] = v6
                v5 += a2
                if v5 >= len(v4):
                    v5 = (v5 - 1) % a2
        return ''.join(v4)
