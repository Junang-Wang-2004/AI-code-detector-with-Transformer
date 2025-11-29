class C1(object):

    def canJump(self, a1):
        v1 = 0
        for v2, v3 in enumerate(a1):
            if v2 > v1:
                break
            v1 = max(v1, v2 + v3)
        return v1 >= len(a1) - 1
