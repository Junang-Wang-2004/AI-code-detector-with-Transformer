import collections

class C1(object):

    def rootCount(self, a1, a2, a3):
        """
        """
        v1 = [0]

        def memoization(a1, a2):
            if (a1, a2) not in memo:
                memo[a1, a2] = int((a2, a1) in lookup)
                for v1 in adj[a1]:
                    if v1 == a2:
                        continue
                    v1[0] += 1
                    memo[a1, a2] += memoization(v1, a1)
            return memo[a1, a2]
        v2 = collections.defaultdict(list)
        for v3, v4 in a1:
            v2[v3].append(v4)
            v2[v4].append(v3)
        v5 = {(v3, v4) for v3, v4 in a2}
        v6 = {}
        return sum((memoization(i, -1) >= a3 for v7 in v2.keys()))
