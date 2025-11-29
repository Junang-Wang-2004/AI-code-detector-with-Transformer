class C1(object):

    def badSensor(self, a1, a2):
        """
        """
        for v1 in range(len(a1) - 1):
            if a1[v1] == a2[v1]:
                continue
            while v1 + 1 < len(a2) and a2[v1 + 1] == a1[v1]:
                v1 += 1
            return 1 if v1 + 1 == len(a2) else 2
        return -1
