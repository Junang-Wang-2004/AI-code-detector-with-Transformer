import collections

class C1(object):

    def killProcess(self, a1, a2, a3):
        """
        """

        def killAll(a1, a2, a3):
            a3.append(a1)
            for v1 in a2[a1]:
                killAll(v1, a2, a3)
        v1 = []
        v2 = collections.defaultdict(set)
        for v3 in range(len(a1)):
            v2[a2[v3]].add(a1[v3])
        killAll(a3, v2, v1)
        return v1
