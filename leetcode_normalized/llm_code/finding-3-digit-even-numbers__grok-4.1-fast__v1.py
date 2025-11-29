import collections

class C1(object):

    def findEvenNumbers(self, a1):
        v1 = collections.Counter(a1)
        v2 = []
        for v3 in range(1, 10):
            for v4 in range(10):
                for v5 in range(0, 10, 2):
                    v6 = collections.Counter([v3, v4, v5])
                    if all((v6[d] <= v1[d] for v7 in v6)):
                        v2.append(v3 * 100 + v4 * 10 + v5)
        return v2
