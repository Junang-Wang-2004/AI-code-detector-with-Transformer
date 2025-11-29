class C1(object):

    def findIntersectionValues(self, a1, a2):
        """
        """
        v1, v2 = (set(a1), set(a2))
        return [sum((x in v2 for v3 in a1)), sum((v3 in v1 for v3 in a2))]
