class C1(object):

    def validPartition(self, a1):
        """
        """
        v1 = [False] * 4
        v1[0] = True
        for v2 in range(len(a1)):
            v1[(v2 + 1) % 4] = False
            if v2 - 1 >= 0 and a1[v2] == a1[v2 - 1]:
                v1[(v2 + 1) % 4] |= v1[(v2 + 1 - 2) % 4]
            if v2 - 2 >= 0 and (a1[v2] == a1[v2 - 1] == a1[v2 - 2] or a1[v2] == a1[v2 - 1] + 1 == a1[v2 - 2] + 2):
                v1[(v2 + 1) % 4] |= v1[(v2 + 1 - 3) % 4]
        return v1[len(a1) % 4]
