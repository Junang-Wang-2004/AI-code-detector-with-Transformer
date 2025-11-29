import collections

class C1(object):

    def maximumInvitations(self, a1):
        """
        """

        def augment(a1, a2, a3, a4):
            for v1 in a1[a2]:
                if v1 in a3:
                    continue
                a3.add(v1)
                if v1 not in a4 or augment(a1, a4[v1], a3, a4):
                    a4[v1] = a2
                    return True
            return False

        def hungarian(a1):
            v1 = {}
            for v2 in a1.keys():
                augment(a1, v2, set(), v1)
            return len(v1)
        v1 = collections.defaultdict(list)
        for v2 in range(len(a1)):
            for v3 in range(len(a1[0])):
                if not a1[v2][v3]:
                    continue
                if len(a1) < len(a1[0]):
                    v1[v2].append(v3)
                else:
                    v1[v3].append(v2)
        return hungarian(v1)
