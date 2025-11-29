class C1(object):

    def finalValueAfterOperations(self, a1):
        """
        """
        return sum((1 if '+' == op[1] else -1 for v1 in a1))
