import collections
import itertools

class C1(object):

    def singleDivisorTriplet(self, a1):
        """
        """

        def check(a1, a2, a3):
            return sum(((a1 + a2 + a3) % x == 0 for v1 in (a1, a2, a3))) == 1
        v1 = collections.Counter(a1)
        return 6 * (sum((v1[a] * v1[b] * v1[c] for v2, v3, v4 in itertools.combinations(list(v1.keys()), 3) if check(v2, v3, v4))) + sum((v1[v2] * (v1[v2] - 1) // 2 * v1[v3] for v2, v3 in itertools.permutations(list(v1.keys()), 2) if check(v2, v2, v3))))
