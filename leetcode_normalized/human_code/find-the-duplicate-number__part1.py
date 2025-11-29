class C1(object):

    def findDuplicate(self, a1):
        """
        """
        v1 = a1[0]
        v2 = a1[a1[0]]
        while v1 != v2:
            v1 = a1[v1]
            v2 = a1[a1[v2]]
        v2 = 0
        while v1 != v2:
            v1 = a1[v1]
            v2 = a1[v2]
        return v1
