class C1(object):

    def asteroidCollision(self, a1):
        """
        """
        v1 = []
        for v2 in a1:
            if v2 > 0:
                v1.append(v2)
                continue
            while v1 and 0 < v1[-1] < -v2:
                v1.pop()
            if v1 and 0 < v1[-1]:
                if v1[-1] == -v2:
                    v1.pop()
                continue
            v1.append(v2)
        return v1
