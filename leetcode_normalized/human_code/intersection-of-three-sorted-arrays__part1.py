from functools import reduce

class C1(object):

    def arraysIntersection(self, a1, a2, a3):
        """
        """
        v1 = []
        v2, v3, v4 = (0, 0, 0)
        while v2 != len(a1) and v3 != len(a2) and (v4 != len(a3)):
            if a1[v2] == a2[v3] == a3[v4]:
                v1.append(a1[v2])
                v2 += 1
                v3 += 1
                v4 += 1
            else:
                v5 = max(a1[v2], a2[v3], a3[v4])
                while v2 != len(a1) and a1[v2] < v5:
                    v2 += 1
                while v3 != len(a2) and a2[v3] < v5:
                    v3 += 1
                while v4 != len(a3) and a3[v4] < v5:
                    v4 += 1
        return v1
