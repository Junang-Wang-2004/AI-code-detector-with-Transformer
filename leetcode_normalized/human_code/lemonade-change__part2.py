import collections

class C1(object):

    def lemonadeChange(self, a1):
        """
        """
        v1, v2 = (0, 0)
        for v3 in a1:
            if v3 == 5:
                v1 += 1
            elif v3 == 10:
                if not v1:
                    return False
                v1 -= 1
                v2 += 1
            elif v2 and v1:
                v2 -= 1
                v1 -= 1
            elif v1 >= 3:
                v1 -= 3
            else:
                return False
        return True
