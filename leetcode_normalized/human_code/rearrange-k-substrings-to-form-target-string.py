import collections

class C1(object):

    def isPossibleToRearrange(self, a1, a2, a3):
        """
        """
        v1 = collections.defaultdict(int)
        v2 = len(a1) // a3
        for v3 in range(0, len(a1), v2):
            v1[a1[v3:v3 + v2]] += 1
            v1[a2[v3:v3 + v2]] -= 1
        return all((v == 0 for v4 in v1.values()))
