import collections

class C1(object):

    def countAnagrams(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3, v4 = [[1] * 2 for v5 in range(3)]

        def lazy_init(a1):
            while len(v3) <= a1:
                v2.append(v2[-1] * len(v3) % v1)
                v3.append(v3[v1 % len(v3)] * (v1 - v1 // len(v3)) % v1)
                v4.append(v4[-1] * v3[-1] % v1)

        def factorial(a1):
            lazy_init(a1)
            return v2[a1]

        def inv_factorial(a1):
            lazy_init(a1)
            return v4[a1]

        def count(a1, a2):
            v1 = 1
            v2 = collections.Counter()
            for v3 in range(a1, a2 + 1):
                v2[a1[v3]] += 1
            v1 = factorial(sum(v2.values()))
            for v4 in v2.values():
                v1 = v1 * inv_factorial(v4) % v1
            return v1
        v6 = 1
        v7 = 0
        for v8 in range(len(a1)):
            if v8 + 1 != len(a1) and a1[v8 + 1] != ' ':
                continue
            v6 = v6 * count(v7, v8) % v1
            v7 = v8 + 2
        return v6
