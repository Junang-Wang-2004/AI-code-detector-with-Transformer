import collections

class C1(object):

    def minReorder(self, a1, a2):
        """
        """
        v1, v2 = (set(), collections.defaultdict(list))
        for v3, v4 in a2:
            v1.add(v3 * a1 + v4)
            v2[v4].append(v3)
            v2[v3].append(v4)
        v5 = 0
        v6 = [(-1, 0)]
        while v6:
            v7, v3 = v6.pop()
            v5 += v7 * a1 + v3 in v1
            for v4 in reversed(v2[v3]):
                if v4 == v7:
                    continue
                v6.append((v3, v4))
        return v5
