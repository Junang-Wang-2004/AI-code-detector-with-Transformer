class C1(object):

    def containsNearbyDuplicate(self, a1, a2):
        v1 = set()
        for v2 in range(len(a1)):
            if a1[v2] in v1:
                return True
            v1.add(a1[v2])
            if v2 >= a2:
                v1.remove(a1[v2 - a2])
        return False
