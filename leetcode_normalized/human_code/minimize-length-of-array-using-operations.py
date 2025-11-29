class C1(object):

    def minimumArrayLength(self, a1):
        """
        """
        v1 = min(a1)
        return (a1.count(v1) + 1) // 2 if all((x % v1 == 0 for v2 in a1)) else 1
