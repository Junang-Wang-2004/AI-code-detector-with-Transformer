class C1(object):

    def maxSelectedElements(self, a1):
        """
        """
        a1.sort()
        v1 = 1
        v2 = [1] * 2
        for v3 in range(1, len(a1)):
            if a1[v3] == a1[v3 - 1]:
                v2[1] = v2[0] + 1
            elif a1[v3] == a1[v3 - 1] + 1:
                v2[0] += 1
                v2[1] += 1
            elif a1[v3] == a1[v3 - 1] + 2:
                v2[0] = v2[1] + 1
                v2[1] = 1
            else:
                v2[0] = v2[1] = 1
            v1 = max(v1, v2[0], v2[1])
        return v1
