class C1(object):

    def asteroidCollision(self, a1):
        """
        """
        v1 = []
        for v2 in a1:
            while v1 and v2 < 0 < v1[-1]:
                if v1[-1] < -v2:
                    v1.pop()
                    continue
                elif v1[-1] == -v2:
                    v1.pop()
                break
            else:
                v1.append(v2)
        return v1
