class C1(object):

    def countSeniors(self, a1):
        """
        """
        return sum((x[-4:-2] > '60' for v1 in a1))
