import collections

class C1(object):

    def distinctNumbers(self, a1, a2):
        """
        """
        v1 = []
        v2 = collections.Counter()
        for v3, v4 in enumerate(a1):
            v2[v4] += 1
            if v3 >= a2:
                v2[a1[v3 - a2]] -= 1
                if not v2[a1[v3 - a2]]:
                    del v2[a1[v3 - a2]]
            if v3 + 1 >= a2:
                v1.append(len(v2))
        return v1
