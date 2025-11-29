import collections

class C1(object):

    def countDistinct(self, a1, a2, a3):
        """
        """
        v1, v2 = (10 ** 9 + 7, 113)

        def check(a1, a2, a3, a4):
            return all((any((a1[a4 + a2] != a1[j + a2] for a2 in range(a3))) for v1 in a2))
        v3 = 0
        v4, v5 = ([0] * len(a1), [0] * len(a1))
        for v6 in range(1, len(a1) + 1):
            v7 = collections.defaultdict(list)
            for v8 in range(len(a1) - v6 + 1):
                v4[v8] += a1[v8 + v6 - 1] % a3 == 0
                if v4[v8] > a2:
                    continue
                v5[v8] = (v5[v8] * v2 + a1[v8 + v6 - 1]) % v1
                if not check(a1, v7[v5[v8]], v6, v8):
                    continue
                v7[v5[v8]].append(v8)
                v3 += 1
        return v3
