class C1(object):

    def addToArrayForm(self, a1, a2):
        """
        """
        a1.reverse()
        v1, v2 = (a2, 0)
        a1[v2] += v1
        v1, a1[v2] = divmod(a1[v2], 10)
        while v1:
            v2 += 1
            if v2 < len(a1):
                a1[v2] += v1
            else:
                a1.append(v1)
            v1, a1[v2] = divmod(a1[v2], 10)
        a1.reverse()
        return a1
