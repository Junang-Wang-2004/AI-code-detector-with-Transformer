class C1(object):

    def check(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            if a1[v2] > a1[(v2 + 1) % len(a1)]:
                v1 += 1
                if v1 > 1:
                    return False
        return True
