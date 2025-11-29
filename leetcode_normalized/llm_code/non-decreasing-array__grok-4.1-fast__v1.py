class C1(object):

    def checkPossibility(self, a1):
        v1 = len(a1)
        for v2 in range(1, v1):
            if a1[v2 - 1] > a1[v2]:
                break
        else:
            return True
        v3 = True
        v4 = v2 < 2 or a1[v2 - 2] <= a1[v2]
        if v4:
            for v5 in range(v2 + 1, v1):
                if a1[v5 - 1] > a1[v5]:
                    v3 = False
                    break
            if v3:
                return True
        v6 = True
        if v2 + 1 < v1:
            if a1[v2 - 1] > a1[v2 + 1]:
                v6 = False
            else:
                for v5 in range(v2 + 2, v1):
                    if a1[v5 - 1] > a1[v5]:
                        v6 = False
                        break
        if v6:
            return True
        return False
