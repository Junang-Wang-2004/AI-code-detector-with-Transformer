class C1(object):

    def findCelebrity(self, a1):
        v1 = 0
        v2 = 1
        while v2 < a1:
            if knows(v1, v2):
                v1 = v2
            v2 += 1
        for v3 in range(a1):
            if v3 != v1 and knows(v1, v3):
                return -1
        for v3 in range(a1):
            if v3 != v1 and (not knows(v3, v1)):
                return -1
        return v1
