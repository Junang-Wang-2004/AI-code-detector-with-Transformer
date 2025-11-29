class C1(object):

    def reversePrefix(self, a1, a2):
        """
        """
        v1 = a1.find(a2)
        return a1[:v1 + 1][::-1] + a1[v1 + 1:]
