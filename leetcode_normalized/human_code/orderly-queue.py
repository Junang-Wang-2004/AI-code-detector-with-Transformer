class C1(object):

    def orderlyQueue(self, a1, a2):
        """
        """
        if a2 == 1:
            return min((a1[i:] + a1[:i] for v1 in range(len(a1))))
        return ''.join(sorted(a1))
