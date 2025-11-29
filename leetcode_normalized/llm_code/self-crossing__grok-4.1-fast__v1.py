class C1(object):

    def isSelfCrossing(self, a1):
        v1 = len(a1)
        if v1 < 4:
            return False
        v2 = a1[0]
        v3 = a1[1]
        v4 = a1[2]
        v5 = a1[3]
        if v5 >= v3 and v2 >= v4:
            return True
        if v1 == 4:
            return False
        v6 = a1[4]
        if v6 >= v4 and v3 >= v5:
            return True
        if v3 == v5 and v2 + v6 >= v4:
            return True
        v7 = 5
        while v7 < v1:
            v8 = a1[v7]
            if v8 >= v5 and v4 >= v6:
                return True
            if v3 <= v5 and v8 + v3 >= v5 and (v6 <= v4) and (v2 + v6 >= v4):
                return True
            v2 = v3
            v3 = v4
            v4 = v5
            v5 = v6
            v6 = v8
            v7 += 1
        return False
