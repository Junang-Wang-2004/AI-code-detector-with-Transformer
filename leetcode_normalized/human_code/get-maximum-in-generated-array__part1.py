v1 = [0, 1]
v2 = [0, 1]

class C1(object):

    def getMaximumGenerated(self, a1):
        """
        """
        if a1 + 1 > len(v2):
            for v1 in range(len(v1), a1 + 1):
                if v1 % 2 == 0:
                    v1.append(v1[v1 // 2])
                else:
                    v1.append(v1[v1 // 2] + v1[v1 // 2 + 1])
                v2.append(max(v2[-1], v1[-1]))
        return v2[a1]
