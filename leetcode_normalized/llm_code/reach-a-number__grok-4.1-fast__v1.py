class C1(object):

    def reachNumber(self, a1):
        a1 = abs(a1)
        v2 = 0
        v3 = 0
        while True:
            v3 += 1
            v2 += v3
            if v2 >= a1 and (v2 - a1) % 2 == 0:
                return v3
