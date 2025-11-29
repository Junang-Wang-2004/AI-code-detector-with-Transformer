class C1(object):

    def plusOne(self, a1):
        """
        """
        for v1 in reversed(range(len(a1))):
            if a1[v1] == 9:
                a1[v1] = 0
            else:
                a1[v1] += 1
                return a1
        a1[0] = 1
        a1.append(0)
        return a1
