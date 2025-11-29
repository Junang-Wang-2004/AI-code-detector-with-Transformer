import collections

class C1(object):

    def minArrivalsToDiscard(self, a1, a2, a3):
        """
        """
        v1 = 0
        v2 = collections.defaultdict(int)
        for v3 in range(len(a1)):
            v2[a1[v3]] += 1
            if v2[a1[v3]] == a3 + 1:
                v2[a1[v3]] -= 1
                a1[v3] = 0
                v1 += 1
            if v3 - a2 + 1 >= 0:
                if a1[v3 - a2 + 1]:
                    v2[a1[v3 - a2 + 1]] -= 1
                    if not v2[a1[v3 - a2 + 1]]:
                        del v2[a1[v3 - a2 + 1]]
        return v1
