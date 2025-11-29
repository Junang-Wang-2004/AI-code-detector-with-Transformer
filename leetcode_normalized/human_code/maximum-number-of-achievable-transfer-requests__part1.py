import itertools

class C1(object):

    def maximumRequests(self, a1, a2):
        """
        """
        for v1 in reversed(range(1, len(a2) + 1)):
            for v2 in itertools.combinations(range(len(a2)), v1):
                v3 = [0] * a1
                for v4 in v2:
                    v3[a2[v4][0]] -= 1
                    v3[a2[v4][1]] += 1
                if all((v2 == 0 for v2 in v3)):
                    return v1
        return 0
