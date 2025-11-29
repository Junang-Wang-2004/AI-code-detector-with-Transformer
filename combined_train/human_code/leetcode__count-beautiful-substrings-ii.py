import collections

class C1(object):

    def beautifulSubstrings(self, a1, a2):
        """
        """
        v1 = set('aeiou')
        v2 = [0] * (len(a1) + 1)
        for v3 in range(len(a1)):
            v2[v3 + 1] = v2[v3] + (+1 if a1[v3] in v1 else -1)
        v4 = 1
        v5 = a2
        for v3 in range(2, a2 + 1):
            if v3 * v3 > a2:
                break
            v6 = 0
            while v5 % v3 == 0:
                v5 //= v3
                v6 += 1
            if v6:
                v4 *= v3 ** ((v6 + 1) // 2 + int(v3 == 2))
        if v5 != 1:
            v4 *= v5 ** ((1 + 1) // 2 + int(v5 == 2))
        v6 = collections.Counter()
        v7 = 0
        for v3, v8 in enumerate(v2):
            v7 += v6[v8, v3 % v4]
            v6[v8, v3 % v4] += 1
        return v7
