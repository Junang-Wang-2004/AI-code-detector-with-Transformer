import collections

class C1(object):

    def medianOfUniquenessArray(self, a1):
        """
        """

        def binary_search(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a1

        def check(a1):
            v1 = 0
            v2 = collections.Counter()
            v3 = 0
            for v4 in range(len(a1)):
                v2[a1[v4]] += 1
                while len(v2) == a1 + 1:
                    v2[a1[v3]] -= 1
                    if v2[a1[v3]] == 0:
                        del v2[a1[v3]]
                    v3 += 1
                v1 += v4 - v3 + 1
            return v1 >= total - v1
        v1 = (len(a1) + 1) * len(a1) // 2
        return binary_search(1, len(set(a1)), check)
