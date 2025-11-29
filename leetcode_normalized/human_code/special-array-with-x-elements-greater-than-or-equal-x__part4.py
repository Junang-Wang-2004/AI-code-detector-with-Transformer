class C1(object):

    def specialArray(self, a1):
        """
        """
        a1.sort(reverse=True)
        for v1 in range(len(a1)):
            if a1[v1] <= v1:
                break
        else:
            v1 += 1
        return -1 if v1 < len(a1) and a1[v1] == v1 else v1
