class C1(object):

    def minOperations(self, a1, a2):
        """
        """
        v1 = min(a1)
        return len(set(a1)) - int(v1 == a2) if v1 >= a2 else -1
