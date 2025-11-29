import collections

class C1(object):

    def minSetSize(self, a1):
        """
        """
        v1 = [0] * len(a1)
        v2 = collections.Counter(a1)
        for v3 in v2.values():
            v1[v3 - 1] += 1
        v4, v5 = (0, 0)
        for v3 in reversed(range(len(a1))):
            if not v1[v3]:
                continue
            v2 = min(v1[v3], ((len(a1) + 1) // 2 - v5 - 1) // (v3 + 1) + 1)
            v4 += v2
            v5 += v2 * (v3 + 1)
            if v5 >= (len(a1) + 1) // 2:
                break
        return v4
