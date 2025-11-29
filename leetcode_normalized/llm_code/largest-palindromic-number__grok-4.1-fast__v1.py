import collections

class C1:

    def largestPalindromic(self, a1):
        v1 = collections.Counter(a1)
        v2 = []
        for v3 in range(9, 0, -1):
            v4 = v1[str(v3)] // 2
            v2.extend([str(v3)] * v4)
        v5 = v1['0'] // 2
        if v2:
            v2.extend(['0'] * v5)
        v6 = ''
        for v3 in range(9, -1, -1):
            if v1[str(v3)] % 2:
                v6 = str(v3)
                break
        v7 = v2[::-1]
        v8 = ''.join(v2) + v6 + ''.join(v7)
        return v8 if v8 else '0'
