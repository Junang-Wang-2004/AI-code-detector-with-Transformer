class C1(object):

    def countSubstrings(self, a1, a2):
        """
        """
        v1 = a1.count(a2)
        return (v1 + 1) * v1 // 2
