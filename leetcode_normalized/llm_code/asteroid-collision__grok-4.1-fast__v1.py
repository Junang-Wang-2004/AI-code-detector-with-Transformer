class C1(object):

    def asteroidCollision(self, a1):
        v1 = []
        for v2 in a1:
            v3 = False
            while v1 and v1[-1] > 0 and (v2 < 0):
                v4 = v1[-1]
                if v4 < -v2:
                    v1.pop()
                else:
                    if v4 == -v2:
                        v1.pop()
                    v3 = True
                    break
            if not v3:
                v1.append(v2)
        return v1
