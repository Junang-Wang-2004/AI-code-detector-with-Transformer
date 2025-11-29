class C1(object):

    def validSubarraySize(self, a1, a2):
        """
        """
        v1 = [-1]
        for v2 in range(len(a1) + 1):
            while v1[-1] != -1 and (v2 == len(a1) or a1[v1[-1]] >= a1[v2]):
                if a1[v1.pop()] * (v2 - 1 - v1[-1]) > a2:
                    return v2 - 1 - v1[-1]
            v1.append(v2)
        return -1
