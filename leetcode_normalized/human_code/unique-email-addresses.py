class C1(object):

    def numUniqueEmails(self, a1):
        """
        """

        def convert(a1):
            v1, v2 = a1.split('@')
            v1 = v1[:v1.index('+')]
            return ''.join([''.join(v1.split('.')), '@', v2])
        v1 = set()
        for v2 in a1:
            v1.add(convert(v2))
        return len(v1)
