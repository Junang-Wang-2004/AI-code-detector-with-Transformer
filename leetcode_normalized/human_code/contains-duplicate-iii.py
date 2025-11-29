import collections

class C1(object):

    def containsNearbyAlmostDuplicate(self, a1, a2, a3):
        if a2 < 0 or a3 < 0:
            return False
        v1 = collections.OrderedDict()
        for v2 in a1:
            if len(v1) > a2:
                v1.popitem(False)
            v3 = v2 if not a3 else v2 // a3
            for v4 in (v1.get(v3 - 1), v1.get(v3), v1.get(v3 + 1)):
                if v4 is not None and abs(v2 - v4) <= a3:
                    return True
            v1[v3] = v2
        return False
