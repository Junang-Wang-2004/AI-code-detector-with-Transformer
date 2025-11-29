class C1(object):

    def getStrongest(self, a1, a2):
        """
        """
        a1.sort()
        v1 = a1[(len(a1) - 1) // 2]
        a1.sort(key=lambda x: (-abs(x - v1), -x))
        return a1[:a2]
