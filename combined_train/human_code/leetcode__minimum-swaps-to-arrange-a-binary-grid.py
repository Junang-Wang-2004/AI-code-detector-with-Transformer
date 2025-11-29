import itertools

class C1(object):

    def minSwaps(self, a1):
        """
        """
        v1 = 0
        for v2 in reversed(range(1, len(a1))):
            v3 = len(a1) - 1 - v2
            while v3 < len(a1):
                v4 = a1[v3]
                if not sum(itertools.islice(v4, len(v4) - v2, len(v4))):
                    break
                v3 += 1
            else:
                return -1
            while v3 != len(a1) - 1 - v2:
                a1[v3], a1[v3 - 1] = (a1[v3 - 1], a1[v3])
                v1 += 1
                v3 -= 1
        return v1
