class C1(object):

    def get(self, a1):
        """
       """
        pass

    def length(self):
        """
       """
        pass

class C2(object):

    def findInMountainArray(self, a1, a2):
        v1 = a2.length()
        v2, v3 = (0, v1 - 1)
        while v2 < v3:
            v4 = (v2 + v3) // 2
            if a2.get(v4) < a2.get(v4 + 1):
                v2 = v4 + 1
            else:
                v3 = v4
        v5 = v2
        v6, v7 = (0, v5)
        while v6 < v7:
            v8 = v6 + (v7 - v6) // 2
            if a2.get(v8) < a1:
                v6 = v8 + 1
            else:
                v7 = v8
        v9 = v6
        if v9 <= v5 and a2.get(v9) == a1:
            return v9
        v6, v7 = (v5, v1 - 1)
        while v6 < v7:
            v8 = v6 + (v7 - v6) // 2
            if a2.get(v8) > a1:
                v6 = v8 + 1
            else:
                v7 = v8
        v9 = v6
        if v9 < v1 and a2.get(v9) == a1:
            return v9
        return -1
