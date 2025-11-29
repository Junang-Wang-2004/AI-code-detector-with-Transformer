class C1(object):

    def nextGreaterElement(self, a1, a2):
        """
        """
        v1, v2 = ([], {})
        for v3 in a2:
            while v1 and v3 > v1[-1]:
                v2[v1.pop()] = v3
            v1.append(v3)
        while v1:
            v2[v1.pop()] = -1
        return [v2[x] for v4 in a1]
