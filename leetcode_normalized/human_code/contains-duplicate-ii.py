class C1(object):

    def containsNearbyDuplicate(self, a1, a2):
        v1 = {}
        for v2, v3 in enumerate(a1):
            if v3 not in v1:
                v1[v3] = v2
            else:
                if v2 - v1[v3] <= a2:
                    return True
                v1[v3] = v2
        return False
