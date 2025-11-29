class C1(object):

    def numberOfSteps(self, a1):
        """
        """
        v1 = 0
        while a1:
            v1 += 2 if a1 % 2 else 1
            a1 //= 2
        return max(v1 - 1, 0)
