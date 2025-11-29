import collections

class C1(object):

    def numBusesToDestination(self, a1, a2, a3):
        """
        """
        if a2 == a3:
            return 0
        v1 = collections.defaultdict(set)
        for v2, v3 in enumerate(a1):
            for v4 in v3:
                v1[v4].add(v2)
        v5 = 1
        v6 = [a2]
        v7 = set([a2])
        while v6:
            v8 = []
            for v4 in v6:
                for v2 in v1[v4]:
                    for v9 in a1[v2]:
                        if v9 in v7:
                            continue
                        if v9 == a3:
                            return v5
                        v8.append(v9)
                        v1[v9].remove(v2)
                        v7.add(v9)
            v6 = v8
            v5 += 1
        return -1
