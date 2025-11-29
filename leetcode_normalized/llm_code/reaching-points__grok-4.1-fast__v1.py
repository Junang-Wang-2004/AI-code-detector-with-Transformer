class C1(object):

    def reachingPoints(self, a1, a2, a3, a4):
        while a3 >= a1 and a4 >= a2:
            if a3 == a1 and a4 == a2:
                return True
            if a4 == a2 and (a3 - a1) % a4 == 0:
                return True
            if a3 == a1 and (a4 - a2) % a3 == 0:
                return True
            if a3 >= a4:
                a3 %= a4
            else:
                a4 %= a3
        return False
