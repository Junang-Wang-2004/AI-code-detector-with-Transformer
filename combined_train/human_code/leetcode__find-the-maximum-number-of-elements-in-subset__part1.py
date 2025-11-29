import collections

class C1(object):

    def maximumLength(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        v2 = {}
        v3 = 0
        for v4 in v1.keys():
            if v4 == 1:
                v3 = max(v3, v1[v4] - (1 if v1[v4] % 2 == 0 else 0))
                continue
            v5 = []
            while v4 not in v2 and v4 in v1 and (v1[v4] >= 2):
                v5.append(v4)
                v4 *= v4
            if v4 not in v2:
                if v4 not in v1:
                    v4 = v5.pop()
                v2[v4] = 1
            v6 = v2[v4]
            while v5:
                v6 += 2
                v2[v5.pop()] = v6
            v3 = max(v3, v6)
        return v3
