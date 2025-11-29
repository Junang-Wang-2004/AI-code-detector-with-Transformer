import collections

class C1(object):

    def majorityElement(self, a1):
        """
        """
        v1, v2, v3 = (3, len(a1), collections.defaultdict(int))
        for v4 in a1:
            v3[v4] += 1
            if len(v3) == v1:
                for v5 in list(v3.keys()):
                    v3[v5] -= 1
                    if v3[v5] == 0:
                        del v3[v5]
        for v4 in list(v3.keys()):
            v3[v4] = 0
        for v4 in a1:
            if v4 in v3:
                v3[v4] += 1
        v6 = []
        for v4 in list(v3.keys()):
            if v3[v4] > v2 / v1:
                v6.append(v4)
        return v6

    def majorityElement2(self, a1):
        """
        """
        return [i[0] for v1 in list(collections.Counter(a1).items()) if v1[1] > len(a1) / 3]
