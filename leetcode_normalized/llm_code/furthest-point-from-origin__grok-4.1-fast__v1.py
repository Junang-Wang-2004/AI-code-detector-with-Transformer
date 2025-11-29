class C1(object):

    def furthestDistanceFromOrigin(self, a1):
        v1 = a1.count('L')
        v2 = a1.count('R')
        v3 = len(a1) - v1 - v2
        v4 = v2 - v1
        return abs(v4) + v3
