import collections
import itertools

class C1(object):

    def rearrangeString(self, a1, a2):
        """
        """
        if not a2:
            return a1
        v1 = collections.Counter(a1)
        v2 = (len(a1) + a2 - 1) // a2
        if not (max(v1.values()) <= v2 and list(v1.values()).count(v2) <= (len(a1) - 1) % a2 + 1):
            return ''
        v3 = [0] * len(a1)
        v4 = 0
        for v5 in itertools.chain((v5 for v5, v6 in v1.items() if v6 == v2), (v5 for v5, v6 in v1.items() if v6 <= v2 - 2), (v5 for v5, v6 in v1.items() if v6 == v2 - 1)):
            for v7 in range(v1[v5]):
                v3[v4] = v5
                v4 += a2
                if v4 >= len(v3):
                    v4 = v4 % a2 + 1
        return ''.join(v3)
