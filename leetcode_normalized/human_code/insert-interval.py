class C1(object):

    def insert(self, a1, a2):
        """
        """
        v1 = []
        v2 = 0
        while v2 < len(a1) and a2[0] > a1[v2][1]:
            v1 += (a1[v2],)
            v2 += 1
        while v2 < len(a1) and a2[1] >= a1[v2][0]:
            a2 = [min(a2[0], a1[v2][0]), max(a2[1], a1[v2][1])]
            v2 += 1
        v1.append(a2)
        v1.extend(a1[v2:])
        return v1
