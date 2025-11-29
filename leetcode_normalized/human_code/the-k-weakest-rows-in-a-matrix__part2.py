import collections

class C1(object):

    def kWeakestRows(self, a1, a2):
        """
        """
        v1 = collections.OrderedDict()
        for v2 in range(len(a1[0])):
            for v3 in range(len(a1)):
                if a1[v3][v2] or v3 in v1:
                    continue
                v1[v3] = True
                if len(v1) == a2:
                    return list(v1.keys())
        for v3 in range(len(a1)):
            if v3 in v1:
                continue
            v1[v3] = True
            if len(v1) == a2:
                break
        return list(v1.keys())
