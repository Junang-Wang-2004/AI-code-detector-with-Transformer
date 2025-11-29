class C1(object):

    def makesquare(self, a1):
        v1 = sum(a1)
        if v1 % 4 != 0:
            return False
        v2 = v1 // 4
        if max(a1) > v2:
            return False
        a1.sort(reverse=True)
        v3 = [0] * 4

        def assign(a1):
            if a1 == len(a1):
                return True
            for v1 in range(4):
                if v3[v1] + a1[a1] > v2:
                    continue
                v3[v1] += a1[a1]
                if assign(a1 + 1):
                    return True
                v3[v1] -= a1[a1]
                if v3[v1] == 0:
                    break
            return False
        return assign(0)
