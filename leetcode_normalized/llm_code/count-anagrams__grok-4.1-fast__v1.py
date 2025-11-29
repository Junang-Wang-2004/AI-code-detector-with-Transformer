import collections

class C1(object):

    def countAnagrams(self, a1):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = [1] * (v2 + 1)
        for v4 in range(1, v2 + 1):
            v3[v4] = v3[v4 - 1] * v4 % v1
        v5 = a1.split()
        v6 = 1
        for v7 in v5:
            v8 = len(v7)
            v9 = collections.Counter(v7)
            v10 = v3[v8]
            for v11 in v9.values():
                v10 = v10 * pow(v3[v11], v1 - 2, v1) % v1
            v6 = v6 * v10 % v1
        return v6
