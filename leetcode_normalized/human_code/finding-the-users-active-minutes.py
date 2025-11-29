import collections

class C1(object):

    def findingUsersActiveMinutes(self, a1, a2):
        """
        """
        v1 = collections.defaultdict(set)
        for v2, v3 in a1:
            v1[v2].add(v3)
        v4 = [0] * a2
        for v5, v6 in v1.items():
            v4[len(v6) - 1] += 1
        return v4
