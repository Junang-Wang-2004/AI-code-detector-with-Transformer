import collections

class C1(object):

    def minChanges(self, a1, a2):
        """
        """

        def one_are_not_from_nums(a1, a2):
            v1 = [a2[i].most_common(1)[0][1] for v2 in range(a2)]
            return len(a1) - (sum(v1) - min(v1))

        def all_are_from_nums(a1, a2):
            v1 = {0: 0}
            for v2 in a2:
                v3 = collections.defaultdict(int)
                for v4 in v1.keys():
                    for v5 in v2.keys():
                        v3[v4 ^ v5] = max(v3[v4 ^ v5], v1[v4] + v2[v5])
                v1 = v3
            return len(a1) - v1[0]
        v1 = [collections.Counter((a1[j] for v2 in range(i, len(a1), a2))) for v3 in range(a2)]
        return min(one_are_not_from_nums(a1, v1), all_are_from_nums(a1, v1))
