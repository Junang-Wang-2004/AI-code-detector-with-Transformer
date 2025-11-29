import collections

class C1(object):

    def isItPossible(self, a1, a2):
        """
        """
        v1 = collections.Counter(a1)
        v2 = collections.Counter(a2)
        for v3 in v1.keys():
            for v4 in v2.keys():
                if v3 == v4:
                    if len(v1) == len(v2):
                        return True
                else:
                    v5, v6 = (len(v1), len(v2))
                    if v1[v3] == 1:
                        v5 -= 1
                    if v4 not in v1:
                        v5 += 1
                    if v2[v4] == 1:
                        v6 -= 1
                    if v3 not in v2:
                        v6 += 1
                    if v5 == v6:
                        return True
        return False
