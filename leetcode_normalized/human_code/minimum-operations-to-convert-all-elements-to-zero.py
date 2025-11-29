class C1(object):

    def minOperations(self, a1):
        """
        """
        v1 = 0
        v2 = [0]
        for v3 in a1:
            while v2 and v2[-1] > v3:
                v2.pop()
            if v2[-1] < v3:
                v1 += 1
                v2.append(v3)
        return v1
