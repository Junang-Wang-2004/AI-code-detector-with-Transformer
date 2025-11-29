import collections

class C1(object):

    def countPairs(self, a1, a2):
        v1 = []
        v2 = 1
        while v2 * v2 <= a2:
            if a2 % v2 == 0:
                v1.append(v2)
                if v2 != a2 // v2:
                    v1.append(a2 // v2)
            v2 += 1
        v1.sort()
        v3 = collections.defaultdict(list)
        for v4, v5 in enumerate(a1):
            v3[v5].append(v4)
        v6 = 0

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        for v7 in v3.values():
            v8 = {d: 0 for v9 in v1}
            for v10 in v7:
                v11 = gcd(v10, a2)
                v12 = a2 // v11
                v6 += v8.get(v12, 0)
                for v9 in v1:
                    if v10 % v9 == 0:
                        v8[v9] += 1
        return v6
