import collections

class C1(object):

    def largestValsFromLabels(self, a1, a2, a3, a4):
        """
        """
        v1 = collections.defaultdict(int)
        v2 = list(zip(a1, a2))
        v2.sort(reverse=True)
        v3 = 0
        for v4, v5 in v2:
            if v1[v5] >= a4:
                continue
            v3 += v4
            v1[v5] += 1
            a3 -= 1
            if a3 == 0:
                break
        return v3
