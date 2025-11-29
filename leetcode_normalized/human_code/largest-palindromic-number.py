import collections

class C1(object):

    def largestPalindromic(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        v2 = []
        for v3 in reversed(range(10)):
            if not v1[str(v3)] // 2 or (v3 == 0 and (not v2)):
                continue
            for v4 in range(v1[str(v3)] // 2):
                v2.append(str(v3))
        v2.append(max([k for v5, v6 in v1.items() if v6 % 2] or ['']))
        for v3 in reversed(range(len(v2) - 1)):
            v2.append(v2[v3])
        return ''.join(v2) or '0'
