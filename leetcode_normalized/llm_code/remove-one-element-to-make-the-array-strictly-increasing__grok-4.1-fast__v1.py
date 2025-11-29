class C1(object):

    def canBeIncreasing(self, a1):
        v1 = len(a1)
        v2 = -1
        for v3 in range(1, v1):
            if a1[v3] <= a1[v3 - 1]:
                if v2 != -1:
                    return False
                v2 = v3
        if v2 == -1:
            return True
        v4 = v2 <= 1 or a1[v2] > a1[v2 - 2]
        v5 = v2 >= v1 - 1 or a1[v2 + 1] > a1[v2 - 1]
        return v4 or v5
